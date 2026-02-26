from datetime import datetime

from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.enums import OrderStatus
from src.schemas.orm_schemas.order_orm import  Order
from src.schemas.dto_schemas.base_schemas.order_dto import OrderDTO, OrderInDTO
from src.schemas.dto_schemas.extended_schemas.extended_order_dto import OrderRelDTO

class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_order: OrderInDTO):
        statement = insert(Order).values(**new_order.model_dump()).returning(Order)
        try:
            result = await self.session.execute(statement)
            model = result.unique().scalar_one()
            created_order = OrderDTO.model_validate(model, from_attributes=True)
            await self.session.commit()
            return created_order
        except:
            return None
    
    async def read_all(self, master_id: int|None, customer_email: str|None, service_id: int|None, status: OrderStatus|None, order_date: datetime|None) -> list:
        order_list = []

        statement = select(Order)

        if master_id:
            statement = statement.filter(Order.master_id == master_id)

        if customer_email:
            statement = statement.filter(Order.customer_email == customer_email)

        if service_id:
            statement = statement.filter(Order.service_id == service_id)

        if status:
            statement = statement.filter(Order.status == status)

        if order_date:
            statement = statement.filter(Order.order_date == order_date)

        result = await self.session.execute(statement)
        order = result.scalars().all()
        for row in order:
            order_list.append(OrderDTO.model_validate(row, from_attributes=True))
        return order_list

    async def read_all_rel(self):
        order_list = []
        statement = select(Order).options(joinedload(Order.master)).options(joinedload(Order.service))
        result = await self.session.execute(statement)
        order = result.scalars().all()
        for row in order:
            order_list.append(OrderRelDTO.model_validate(row, from_attributes=True))
        return order_list
    
    async def read_by_id(self, id: int):
        statement = select(Order).filter(Order.order_id == id)
        result = await self.session.execute(statement)
        model = result.scalars().one_or_none()
        if model:
            return OrderDTO.model_validate(model, from_attributes=True)
        return None
    
    async def read_by_id_rel(self, id: int):
        statement = select(Order).filter(Order.order_id == id).options(joinedload(Order.master)).options(joinedload(Order.service))
        result = await self.session.execute(statement)
        model = result.scalars().all()
        return OrderRelDTO.model_validate(model, from_attributes=True)
    
    async def update(self, id: int, new_order: OrderInDTO):
        statement = select(Order).filter(Order.order_id == id)
        result = await self.session.execute(statement)
        changed_order = result.scalar_one()
        changed_order.service_id = new_order.service_id
        changed_order.master_id = new_order.master_id
        changed_order.customer_email = new_order.customer_email
        changed_order.customer_addres = new_order.customer_addres
        changed_order.status = new_order.status
        updated_order = OrderDTO.model_validate(changed_order, from_attributes=True)
        await self.session.commit()
        return updated_order
    
    async def change_status_to_denied(self, id: int):
        statement = select(Order).filter(Order.order_id == id)
        result = await self.session.execute(statement)
        changed_order = result.scalar_one()
        changed_order.status = OrderStatus.denied
        updated_order = OrderDTO.model_validate(changed_order, from_attributes=True)
        await self.session.commit()
        return updated_order
    
    async def change_status_to_completed(self, id: int):
        statement = select(Order).filter(Order.order_id == id)
        result = await self.session.execute(statement)
        changed_order = result.scalar_one()
        changed_order.status = OrderStatus.completed
        updated_order = OrderDTO.model_validate(changed_order, from_attributes=True)
        await self.session.commit()
        return updated_order      
    
    async def delete(self, id: int):
        deleted_order = await self.session.get(Order, id)
        await self.session.delete(deleted_order)
        await self.session.commit()
        return