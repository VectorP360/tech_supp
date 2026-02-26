from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.dto_schemas.base_schemas.master_dto import MasterInDTO
from src.enums import MasterStatus, Data_search
from src.repository.master_repository import MasterRepository

class MasterService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = MasterRepository(session=session)

    async def create_master(self, new_master: MasterInDTO):
        created_master = await self.repository.create(new_master=new_master)
        if created_master:
            return created_master
        return Data_search.creating_error
    
    async def get_all_masters(self, status: MasterStatus|None):
        founded = await self.repository.read_all(status=status)
        return founded
    
    async def get_master_by_id(self, id: int):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            return founded
        return Data_search.not_found
    
    async def change_phone(self, id: int, new_phone: str):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            return await self.repository.update(id=id, new_master=MasterInDTO(name=founded.name, phone_number=new_phone, status=founded.status))
        return Data_search.not_found
    
    async def change_status(self, id: int):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            if founded.status == MasterStatus.busy:
                return await self.repository.update(id=id, new_master=MasterInDTO(name=founded.name, phone_number=founded.phone_number, status=MasterStatus.free))
            elif founded.status == MasterStatus.free:
                return await self.repository.update(id=id, new_master=MasterInDTO(name=founded.name, phone_number=founded.phone_number, status=MasterStatus.busy))
        return Data_search.not_found
    
    async def delete_master(self, id: int):
        check = await self.repository.read_by_id(id)
        if check:
            await self.repository.delete(id=id)
            return True
        return False