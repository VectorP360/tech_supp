from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.enums import ServiceType
from src.schemas.orm_schemas.service_orm import  Service
from src.schemas.dto_schemas.base_schemas.service_dto import ServiceDTO, ServiceInDTO
from src.schemas.dto_schemas.extended_schemas.extended_service_dto import ServiceRelDTO

class ServiceRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_service: ServiceInDTO):
        statement = insert(Service).values(**new_service.model_dump()).returning(Service)
        try:
            result = await self.session.execute(statement)
            model = result.unique().scalar_one()
            created_service = ServiceDTO.model_validate(model, from_attributes=True)
            await self.session.commit()
            return created_service
        except:
            return None
    
    async def read_all(self, service_type: ServiceType|None):
        service_list = []
        statement = select(Service)
        if service_type:
            statement = statement.filter(Service.service_type == service_type)
        result = await self.session.execute(statement)
        service = result.scalars().all()
        for row in service:
            service_list.append(ServiceDTO.model_validate(row, from_attributes=True))
        if not service_list:
            return None
        return service_list

    async def read_all_rel(self):
        service_list = []
        statement = select(Service).options(selectinload(Service.order)).options(selectinload(Service.service_detail))
        result = await self.session.execute(statement)
        service = result.scalars().all()
        for row in service:
            service_list.append(ServiceRelDTO.model_validate(row, from_attributes=True))
        return service_list
    
    async def read_by_id(self, id: int):
        statement = select(Service).filter(Service.service_id == id)
        result = await self.session.execute(statement)
        model = result.scalars().one_or_none()
        if model:
            return ServiceDTO.model_validate(model, from_attributes=True)
        return None
    
    async def read_by_id_rel(self, id: int):
        statement = select(Service).filter(Service.service_id == id).options(selectinload(Service.order)).options(selectinload(Service.service_detail))
        result = await self.session.execute(statement)
        model = result.scalars().all()
        return ServiceRelDTO.model_validate(model, from_attributes=True)
    
    async def update(self, id: int, new_service: ServiceInDTO):
        statement = select(Service).filter(Service.service_id == id)
        result = await self.session.execute(statement)
        changed_service = result.scalar_one()
        changed_service.service_type = new_service.service_type
        changed_service.cost = new_service.cost
        updated = ServiceDTO.model_validate(changed_service, from_attributes=True)
        await self.session.commit()
        return updated
    
    async def delete(self, id: int):
        deleted_service = await self.session.get(Service, id)
        await self.session.delete(deleted_service)
        await self.session.commit()
        return