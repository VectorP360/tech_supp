from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.dto_schemas.base_schemas.detail_dto import DetailInDTO

from src.repository.detail_repository import DetailRepository

from src.enums import Data_search

class DetailService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = DetailRepository(session)

    async def create(self, new_detail: DetailInDTO):
        created_detail = await self.repository.create(new_detail)
        if created_detail:
            return created_detail
        return Data_search.creating_error
    
    async def get_details(self, tech_type_id: int | None):
        founded = await self.repository.read_all(tech_type_id)
        if founded:
            return founded
        return Data_search.not_found
    
    async def get_detail_by_id(self, id: int):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            return founded
        return Data_search.not_found
    
    async def change_detail_cost(self, id: int, new_cost: int):
        founded_detail = await self.repository.read_by_id(id=id)
        if founded_detail:
            changed_detail = await self.repository.update(id=id, new_detail=DetailInDTO(tech_type_id=founded_detail.tech_type_id, name = founded_detail.name, cost=new_cost))
            return changed_detail
        return Data_search.not_found
    
    async def delete_detail(self, id: int):
        await self.repository.delete(id=id)
        check = await self.repository.read_by_id(id)
        if check:
            return False
        return True
        