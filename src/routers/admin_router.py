from fastapi import APIRouter
from fastapi import Query
from src.repository.admin_repository import AdminRepository, AdminInDTO
from src.services.admin_service import AdminService
from src.enums import Properties

from src.database import async_session_factory

router = APIRouter(prefix="/admins", tags=["Админы"])

@router.post("/new")
async def add(login: str, password: str, properties: Properties):
    new_admin = AdminInDTO(login=login, password=password, properties=properties)
    async with async_session_factory() as session:
        added_admin = await AdminService(session).create_admin(new_admin)
        return added_admin

@router.get("")
async def get_all_admins(property: Properties|None = Query(None)):
    async with async_session_factory() as session:
        return await AdminService(session).get_all_admins(property)

@router.get("/{id}")
async def get_admins_by_id(id: int):
    async with async_session_factory() as session:
        return await AdminService(session).get_admin_by_id(id)
    
@router.put("/change_property")
async def change_admin_property(id: int, new_property: Properties):
    async with async_session_factory() as session:
        return await AdminService(session).change_properties(id=id , new_property=new_property)
    
@router.put("/change_login_password")
async def change_admin_login_password(id: int, new_login: str, new_password: str):
    async with async_session_factory() as session:
        return await AdminService(session).change_login_password(id=id, new_login=new_login, new_password=new_password)
    
@router.delete("/rip_admin")
async def delete_admin(id: int):
    async with async_session_factory() as session:
        return await AdminService(session).delete_admin(id=id)