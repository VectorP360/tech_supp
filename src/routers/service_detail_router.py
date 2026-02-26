from fastapi import APIRouter
from fastapi import Query
from src.services.service_detail_service import ServiceDetailService
from src.repository.service_detail_repository import ServiceDetailInDTO

from src.database import async_session_factory

router = APIRouter(prefix="/service_detail", tags=["Сервис - Деталь"])

@router.post("/new")
async def add(service_id: int, detail_id: int):
    new_service_detail = ServiceDetailInDTO(service_id=service_id, detail_id=detail_id)
    async with async_session_factory() as session:
        added_service_detail = await ServiceDetailService(session).create_service_detail(new_service_detail=new_service_detail)
        return added_service_detail
    
@router.get("")
async def get_all_service_detail(service_id: int|None = Query(None), detail_id: int|None = Query(None)):
    async with async_session_factory() as session:
        return await ServiceDetailService(session).get_service_detail(service_id=service_id, detail_id=detail_id)
    
@router.get("/{id}")
async def get_by_id(id: int):
    async with async_session_factory() as session:
        return await ServiceDetailService(session).get_service_detail_by_id(id=id)
    
@router.delete("/delete")
async def delete_service_detail(id: int):
    async with async_session_factory() as session:
        return await ServiceDetailService(session).delete_service_detail(id=id)