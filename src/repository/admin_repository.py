from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.orm_schemas.admin_orm import Admin
from src.schemas.dto_schemas.base_schemas.admin_dto import AdminInDTO, AdminDTO
from src.enums import Properties

class AdminRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_admin: AdminInDTO):
        statement = insert(Admin).values(**new_admin.model_dump()).returning(Admin)
        try:
            result = await self.session.execute(statement)
            model = result.unique().scalar_one()
            added_admin = AdminDTO.model_validate(model, from_attributes=True)
            await self.session.commit()
            return added_admin
        except:
            return None

    async def read_all(self, property: Properties|None):
        admin_list = []
        statement = select(Admin)
        if property:
            statement= statement.filter(Admin.properties == property)
        result = await self.session.execute(statement)
        admin = result.scalars().all()
        for row in admin:
            admin_list.append(AdminDTO.model_validate(row, from_attributes=True))
        return admin_list

    async def read_by_id(self, id: int):
        statement = select(Admin).filter(Admin.admin_id == id)
        result = await self.session.execute(statement)
        model = result.scalar_one_or_none()
        if model:
            return AdminDTO.model_validate(model, from_attributes=True)
        return None

    async def update(self, id: int, new_admin: AdminInDTO):
        statement = select(Admin).filter(Admin.admin_id == id)
        result = await self.session.execute(statement)
        changed_admin = result.scalar_one()

        changed_admin.login = new_admin.login
        changed_admin.password = new_admin.password
        changed_admin.properties = new_admin.properties
        
        result = AdminDTO.model_validate(obj=changed_admin, from_attributes=True)
        await self.session.commit()
        return result

    async def delete(self, id: int):
        statement = select(Admin).filter(Admin.admin_id == id)
        result = await self.session.execute(statement)
        deleted_admin = result.scalar_one()
        await self.session.delete(deleted_admin)
        await self.session.commit()
        return 