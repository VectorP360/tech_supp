from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.dto_schemas.base_schemas.order_dto import OrderInDTO, OrderDTO
from src.schemas.dto_schemas.base_schemas.master_dto import MasterInDTO
from src.enums import Data_search, OrderStatus, MasterStatus
from src.repository.order_repository import OrderRepository
from src.repository.master_repository import MasterRepository

class OrderService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = OrderRepository(session=session)

    async def create_order(self, customer_email: str, customer_addres: str, service_id: int):
        free_master = await MasterRepository(self.session).read_by_freedom()
        if not free_master:
            return Data_search.no_free_masters
        await MasterRepository(self.session).change_status_to_busy(id=free_master.master_id)
        
        master_id = free_master.master_id
        order_date = datetime.now()
        status = OrderStatus.WIP

        created_order = await self.repository.create(new_order=OrderInDTO(service_id=service_id,
                                                                     customer_email=customer_email,
                                                                     customer_addres=customer_addres,
                                                                     order_date=order_date,
                                                                     status=status,
                                                                     master_id=master_id))
        
        if created_order:
            return created_order
        return Data_search.creating_error
    

    async def get_orders(self, master_id: int|None, customer_email: str|None, service_id: int|None, status: OrderStatus|None, order_date: datetime|None):
        founded_orders = await self.repository.read_all(master_id, customer_email, service_id, status, order_date)
        if founded_orders:
            return founded_orders
        return Data_search.not_found
    
    async def get_order_by_id(self, id: int):
        founded_order = await self.repository.read_by_id(id=id)
        if founded_order:
            return founded_order
        return Data_search.not_found

    async def change_status(self, id: int, status: OrderStatus):
        founded_order = await self.repository.read_by_id(id=id)
        if founded_order:
            if status == OrderStatus.denied:
                changed_order =  await self.repository.change_status_to_denied(id=id)
                await MasterRepository(self.session).change_status_to_free(id=founded_order.master_id)
                return changed_order
            elif status == OrderStatus.completed:
                changed_order = await self.repository.change_status_to_completed(id=id)
                await MasterRepository(self.session).change_status_to_free(id=founded_order.master_id)
                return changed_order
        return Data_search.not_found
        

    async def delete_order(self, id: int):
        check = await self.repository.read_by_id(id)
        if check:
            await self.repository.delete(id=id)
            return True
        return False