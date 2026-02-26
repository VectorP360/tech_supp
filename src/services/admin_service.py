from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.dto_schemas.base_schemas.admin_dto import AdminInDTO
from src.repository.admin_repository import AdminRepository
from src.enums import Properties, Data_search

class AdminService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = AdminRepository(session)

    async def create_admin(self, new_admin: AdminInDTO):
        created_admin = await self.repository.create(new_admin=new_admin)
        if created_admin:
            return created_admin
        return Data_search.creating_error
    
    async def get_all_admins(self, property: Properties|None):
        founded = await self.repository.read_all(property)
        return founded
    
    async def get_admin_by_id(self, id: int):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            return founded
        return Data_search.not_found
    
    async def change_properties(self, id: int, new_property: Properties):
        founded = await self.repository.read_by_id(id=id)
        if founded: 
            changed = await self.repository.update(id=id, new_admin=AdminInDTO(login=founded.login, password=founded.password, properties=new_property))
            return changed
        return Data_search.not_found
    
    async def change_login_password(self, id:int, new_login: str, new_password: str):
        founded = await self.repository.read_by_id(id=id)
        if founded:
            changed = await self.repository.update(id=id, new_admin=AdminInDTO(login=new_login, password=new_password, properties=founded.properties))
            return changed
        return Data_search.not_found
    
    async def delete_admin(self, id: int):
        await self.repository.delete(id=id)
        check = await self.repository.read_by_id(id)
        if check:
            return False
        return True