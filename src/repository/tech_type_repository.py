from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.orm_schemas.tech_type_orm import TechType
from src.schemas.dto_schemas.base_schemas.tech_type_dto import TechTypeDTO, TechTypeInDTO
from src.schemas.dto_schemas.extended_schemas.extended_tech_type_dto import TechTypeRelDTO

class TechTypeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_tech_type: TechTypeInDTO):
        statement = insert(TechType).values(**new_tech_type.model_dump()).returning(TechType)
        result = await self.session.execute(statement)
        model = result.unique().scalar_one()
        added_tech_type = TechTypeDTO.model_validate(model, from_attributes=True)
        await self.session.commit()
        return added_tech_type
    
    async def read_all(self):
        tech_type_list = []
        statement = select(TechType)
        result = await self.session.execute(statement)
        tech_type = result.scalars().all()
        for row in tech_type:
            tech_type_list.append(TechTypeDTO.model_validate(row, from_attributes=True))
        return tech_type_list
    
    async def read_by_id(self, id: int):
        statement = select(TechType).filter(TechType.tech_type_id == id)
        result = await self.session.execute(statement)
        model = result.scalars().one_or_none()
        if model:
            return TechTypeDTO.model_validate(model, from_attributes=True)
        return None

    async def update(self, id: int, new_tech_type: TechTypeInDTO):
        statement = select(TechType).filter(TechType.tech_type_id == id)
        result = await self.session.execute(statement)
        changed_tech_type = result.scalar_one()
        changed_tech_type.name = new_tech_type.name
        updated_tech_type = TechTypeDTO.model_validate(changed_tech_type, from_attributes=True)
        await self.session.commit()
        return updated_tech_type
    
    async def delete(self, id: int):
        deleted_tech_type = await self.session.get(TechType, id)
        await self.session.delete(deleted_tech_type)
        await self.session.commit()
        return