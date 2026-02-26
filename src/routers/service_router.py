from fastapi import APIRouter, Query
from src.schemas.dto_schemas.base_schemas.service_dto import ServiceInDTO
from src.services.service_service import ServiceService
from src.enums import ServiceType

from src.database import async_session_factory

router = APIRouter(prefix="/services", tags=["Сервисы"])

@router.post("/new")
async def add(service_type: ServiceType, name:str, cost: int):
    new_service = ServiceInDTO(service_type=service_type, name=name, cost=cost)
    async with async_session_factory() as session:
        added_service = await ServiceService(session).create_service(new_service=new_service)
        return added_service
    
@router.get("/")
async def get_all_services(service_type: ServiceType|None = Query(None)):
    async with async_session_factory() as session:
        founded = await ServiceService(session=session).get_all_service(service_type=service_type)
        return founded
    
@router.get("/{id}")
async def get_service_by_id(id: int):
    async with async_session_factory() as session:
        founded = await ServiceService(session=session).get_service_by_id(id=id)
        return founded
    
@router.put("/change_cost")
async def change_service_cost(id: int, new_cost: int):
    async with async_session_factory() as session:
        changed = await ServiceService(session).change_cost(id=id, new_cost=new_cost)
        return changed
    
@router.delete("/delete_service")
async def delete_service(id: int):
    async with async_session_factory() as session:
        return await ServiceService(session).delete_service(id=id)
