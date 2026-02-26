# Ха-ха сервис_сервис
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.dto_schemas.base_schemas.service_dto import ServiceInDTO
from src.enums import ServiceType, Data_search
from src.repository.service_repository import ServiceRepository

class ServiceService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = ServiceRepository(session)

    async def create_service(self, new_service: ServiceInDTO):
        created_service = await self.repository.create(new_service=new_service)
        if created_service:
            return created_service
        return Data_search.creating_error

    async def get_all_service(self, service_type: ServiceType|None):
        founded = await self.repository.read_all(service_type)
        if founded:
            return founded
        return Data_search.not_found
    
    async def get_service_by_id(self, id: int):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            return founded
        return Data_search.not_found
    
    async def change_cost(self, id:int, new_cost: int):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            return await self.repository.update(id=id, new_service=ServiceInDTO(service_type=founded.service_type, name=founded.name, cost=new_cost))
        return Data_search.not_found
    
    async def delete_service(self, id: int):
        check = await self.repository.read_by_id(id=id)
        if check:
            await self.repository.delete(id=id)
            return True
        return False