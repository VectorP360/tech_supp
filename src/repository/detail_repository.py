from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.orm_schemas.detail_orm import Detail
from src.schemas.dto_schemas.base_schemas.detail_dto import DetailDTO, DetailInDTO
from src.schemas.dto_schemas.extended_schemas.extended_detail_dto import DetailRelDTO, DetailTechRelDTO, DetailExtendedViewDTO

class DetailRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_detail: DetailInDTO):
        statement = insert(Detail).values(**new_detail.model_dump()).returning(Detail)
        try:
            result = await self.session.execute(statement)
            model = result.unique().scalar_one()
            added_detail = DetailDTO.model_validate(model, from_attributes=True)
            await self.session.commit()
            return added_detail
        except:
            return None
    
    async def read_all(self, tech_type_id: int | None):
        detail_list = []
        
        statement = select(Detail).options(joinedload(Detail.tech_type))
        if tech_type_id:
            statement = statement.filter(Detail.tech_type_id==tech_type_id)

        result = await self.session.execute(statement)
        detail = result.scalars().all()
        for row in detail:
            detail_list.append(DetailExtendedViewDTO(
                tech_type_id=row.tech_type_id,
                tech_type_name=row.tech_type.name,
                name=row.name, 
                cost=row.cost, 
                detail_id=row.detail_id, 
            ))

        if not detail_list:
            return None
        return detail_list

    async def read_all_rel(self):
        detail_list = []
        statement = select(Detail).options(joinedload(Detail.tech_type)).options(selectinload(Detail.service_detail))
        result = await self.session.execute(statement)
        detail = result.scalars().all()
        for row in detail:
            detail_list.append(DetailRelDTO.model_validate(row, from_attributes=True))
        return detail_list
    
    async def read_rel_tech(self):
        detail_list = []
        statement = select(Detail).options(joinedload(Detail.tech_type))
        result = await self.session.execute(statement)
        rows = result.scalars().all()
        
        for row in rows:
            detail_list.append(
                DetailExtendedViewDTO(
                    tech_type_id=row.tech_type_id, 
                    name=row.name, 
                    cost=row.cost, 
                    detail_id=row.detail_id, 
                    tech_type_name=row.tech_type.name)
                )
        
        return detail_list
    
    async def read_by_id(self, id: int):
        statement = select(Detail).filter(Detail.detail_id == id)
        result = await self.session.execute(statement)
        detail = result.scalars().one_or_none()
        if detail:
            return DetailDTO.model_validate(detail, from_attributes=True)
        return None
    
    async def read_by_id_rel(self, id: int):
        statement = select(Detail).filter(Detail.detail_id == id).options(joinedload(Detail.tech_type)).options(selectinload(Detail.service_detail))
        result = await self.session.execute(statement)
        master = result.scalars().all()
        return DetailRelDTO.model_validate(master, from_attributes=True)
    
    async def update(self, id: int, new_detail: DetailInDTO):
        statement = select(Detail).filter(Detail.detail_id == id)
        result = await self.session.execute(statement)
        changed_detail = result.scalar_one()
        changed_detail.name = new_detail.name
        changed_detail.tech_type_id = new_detail.tech_type_id
        changed_detail.cost = new_detail.cost
        updated_detail = DetailDTO.model_validate(changed_detail, from_attributes=True)
        await self.session.commit()
        return updated_detail
    
    async def delete(self, id: int):
        deleted_detail = await self.session.get(Detail, id)
        await self.session.delete(deleted_detail)
        await self.session.commit()
        return