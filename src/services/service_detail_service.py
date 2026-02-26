#Ха-ха, теперь это сервис-деталь-сервис... Надо поработать надд названиями файлов.
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.dto_schemas.base_schemas.service_detail_dto import ServiceDetailInDTO
from src.enums import Data_search
from src.repository.service_detail_repository import ServiceDetailRepository

class ServiceDetailService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = ServiceDetailRepository(session)

    async def create_service_detail(self, new_service_detail: ServiceDetailInDTO):
        created_service_detail = await self.repository.create(new_service_detail=new_service_detail)
        if created_service_detail:
            return created_service_detail
        return Data_search.creating_error

    async def get_service_detail(self, service_id: int|None, detail_id: int|None):
        founded = await self.repository.read_all(service_id=service_id, detail_id=detail_id)
        if founded:
            return founded
        return Data_search.not_found
    
    async def get_service_detail_by_id(self, id: int):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            return founded
        return Data_search.not_found
    
    async def delete_service_detail(self, id: int):
        check = await self.repository.read_by_id(id=id)
        if check:
            await self.repository.delete(id=id)
            return True
        return False