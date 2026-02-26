from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.dto_schemas.base_schemas.tech_type_dto import TechTypeInDTO

from src.repository.tech_type_repository import TechTypeRepository

class TechTypeService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = TechTypeRepository(session)

    async def create(self, new_tech_type: TechTypeInDTO):
        created_tech_type = await self.repository.create(new_tech_type=new_tech_type)
        return created_tech_type
    
    async def get_all_types(self):
        founded_types = await self.repository.read_all()
        return founded_types
    
    async def get_type_by_id(self, id: int):
        founded_type = await self.repository.read_by_id(id)
        if founded_type:
            return founded_type
        return {"message" : "Элемент не найден"}
    
    async def change_type_name(self, id: int, new_name: str):
        updated_type = await self.repository.update(id, new_tech_type=TechTypeInDTO(name=new_name))
        return updated_type
    
    async def delete_type(self, id: int):
        await self.repository.delete(id)
        check = await self.repository.read_by_id(id)
        if check:
            return False
        return True