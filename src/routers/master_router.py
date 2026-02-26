from fastapi import APIRouter
from fastapi import Query
from src.services.master_service import MasterService
from src.repository.master_repository import MasterInDTO, MasterRepository
from src.enums import MasterStatus

from src.database import async_session_factory

router = APIRouter(prefix="/masters", tags=["Мастера"])

@router.post("/new")
async def add(name: str, phone_number: str, status: MasterStatus):
    new_master = MasterInDTO(name=name, phone_number=phone_number, status=status)
    async with async_session_factory() as session:
        added_master = await MasterService(session).create_master(new_master=new_master)
        return added_master

@router.get("")
async def get_all_masters(status: MasterStatus|None = Query(None)):
    async with async_session_factory() as session:
        return await MasterService(session).get_all_masters(status=status)

@router.get("/{id}")
async def get_masters_by_id(id: int):
    async with async_session_factory() as session:
        return await MasterService(session).get_master_by_id(id)
    
@router.put("/change_phone")
async def change_phone(id: int, new_phone: str):
    async with async_session_factory() as session:
        return await MasterService(session).change_phone(id=id, new_phone = new_phone)
    
@router.put("/change_status")
async def change_status(id: int):
    async with async_session_factory() as session:
        return await MasterService(session).change_status(id=id)

@router.delete("/rip_master")
async def delete_master(id: int):
    async with async_session_factory() as session:
        return await MasterService(session).delete_master(id)