from fastapi import APIRouter
from fastapi import Query
from src.schemas.dto_schemas.base_schemas.detail_dto import DetailInDTO
from src.services.detail_service import DetailService
from src.database import async_session_factory

router = APIRouter(prefix="/details", tags=["Детали"])

@router.post("/new")
async def add(tech_type_id: int, name: str, cost: int):
    new_detail = DetailInDTO(tech_type_id=tech_type_id, name=name, cost=cost)
    async with async_session_factory() as session:
        added_detail = await DetailService(session).create(new_detail)
        return added_detail

@router.get("")
async def get_all_details(tech_type_id: int | None = Query(None)):
    async with async_session_factory() as session:
        return await DetailService(session).get_details(tech_type_id)

@router.get("/{id}")
async def get_details_by_id(id: int):
    async with async_session_factory() as session:
        return await DetailService(session).get_detail_by_id(id)
    
@router.put("/change_cost_of_detail")
async def change_detail(id: int, cost: int):
    async with async_session_factory() as session:
        return await DetailService(session).change_detail_cost(id=id, new_cost=cost)
    
@router.delete("/delete_detail")
async def delete_master(id: int):
    async with async_session_factory() as session:
        return await DetailService(session).delete_detail(id)