from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.orm_schemas.master_orm import Master
from src.schemas.dto_schemas.base_schemas.master_dto import MasterInDTO, MasterDTO 
from src.schemas.dto_schemas.extended_schemas.extended_master_dto import MasterRelDTO
from src.enums import MasterStatus

class MasterRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_master: MasterInDTO):
        statement = insert(Master).values(**new_master.model_dump()).returning(Master)
        try:
            result = await self.session.execute(statement)
            model = result.unique().scalar_one()
            added_master = MasterDTO.model_validate(model, from_attributes=True)
            await self.session.commit()
            return added_master
        except:
            return None
    
    async def read_all(self, status: MasterStatus|None) -> list[MasterDTO]|None:
        master_list = []
        statement = select(Master)

        if status:
            statement = statement.filter(Master.status == status)

        result = await self.session.execute(statement)
        master = result.scalars().all()
        for row in master:
            master_list.append(MasterDTO.model_validate(row, from_attributes=True))

        if not master_list:
            return None
        
        return master_list

    async def read_all_rel(self):
        master_list = []
        statement = select(Master).options(selectinload(Master.order))
        result = await self.session.execute(statement)
        master = result.scalars().all()
        for row in master:
            master_list.append(MasterRelDTO.model_validate(row, from_attributes=True))
        return master_list
    
    async def read_by_freedom(self):
        statement = select(Master).filter(Master.status == MasterStatus.free).limit(1)
        result = await self.session.execute(statement)
        master = result.scalar_one_or_none()
        if master:
            return MasterDTO.model_validate(master, from_attributes=True)
        return None

    async def read_by_id(self, id: int):
        statement = select(Master).filter(Master.master_id == id)
        result = await self.session.execute(statement)
        master = result.scalars().one_or_none()
        if master:
            return MasterDTO.model_validate(master, from_attributes=True)
        return None
    
    async def read_by_id_rel(self, id: int):
        statement = select(Master).filter(Master.master_id == id).options(selectinload(Master.order))
        result = await self.session.execute(statement)
        master = result.scalars().all()
        await self.session.commit()
        return MasterRelDTO.model_validate(master, from_attributes=True)
    
    async def update(self, id: int, new_master: MasterInDTO):
        statement = select(Master).filter(Master.master_id == id)
        result = await self.session.execute(statement)
        changed_master = result.scalar_one_or_none()
        if not changed_master:
            return None
        changed_master.name = new_master.name
        changed_master.phone_number = new_master.phone_number
        changed_master.status = new_master.status
        updated_master = MasterDTO.model_validate(changed_master, from_attributes=True)
        await self.session.commit()
        return updated_master
    
    async def change_status_to_free(self, id: int):
        statement = select(Master).filter(Master.master_id == id)
        result = await self.session.execute(statement)
        changed_master = result.scalar_one_or_none()
        if not changed_master:
            return None
        changed_master.status = MasterStatus.free
        updated_master = MasterDTO.model_validate(changed_master, from_attributes=True)
        await self.session.commit()
        return updated_master
    
    async def change_status_to_busy(self, id: int):
        statement = select(Master).filter(Master.master_id == id)
        result = await self.session.execute(statement)
        changed_master = result.scalar_one_or_none()
        if not changed_master:
            return None
        changed_master.status = MasterStatus.busy
        updated_master = MasterDTO.model_validate(changed_master, from_attributes=True)
        await self.session.commit()
        return updated_master

    async def delete(self, id: int):
        deleted_master = await self.session.get(Master, id)
        await self.session.delete(deleted_master)
        await self.session.commit()
        return