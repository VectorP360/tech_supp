from fastapi import APIRouter
from src.repository.tech_type_repository import TechTypeInDTO, TechTypeRepository
from src.services.tech_type_srvice import TechTypeService

from src.database import async_session_factory

router = APIRouter(prefix="/tech_types", tags=["Типы техники"])

@router.post("/new")
async def add(name: str):
    new_tech_type = TechTypeInDTO(name=name)
    async with async_session_factory() as session:
        added_tech_type = await TechTypeService(session=session).create(new_tech_type=new_tech_type)
        return added_tech_type

@router.get("")
async def get_all_tech_type():
    async with async_session_factory() as session:
        return await TechTypeService(session=session).get_all_types()

@router.get("/{id}")
async def get_tech_type_by_id(id: int):
    async with async_session_factory() as session:
        return await TechTypeService(session=session).get_type_by_id(id)
    
@router.put("/change_full")
async def change_tech_type(id: int, update_tech_type: TechTypeInDTO):
    async with async_session_factory() as session:
        return await TechTypeService(session).change_type_name(id=id, new_name=update_tech_type.name)
    
@router.delete("/delete_tech_type")
async def delete_tech_type(id: int):
    async with async_session_factory() as session:
        return await TechTypeService(session).delete_type(id=id)