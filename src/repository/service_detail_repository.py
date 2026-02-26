from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.orm_schemas.service_detail_orm import ServiceDetail
from src.schemas.dto_schemas.base_schemas.service_detail_dto import ServiceDetailDTO, ServiceDetailInDTO
from src.schemas.dto_schemas.extended_schemas.extended_service_detail_dto import ServiceDetailRelDTO

class ServiceDetailRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_service_detail: ServiceDetailInDTO):
        statement = insert(ServiceDetail).values(**new_service_detail.model_dump()).returning(ServiceDetail)
        try:
            result = await self.session.execute(statement)
            model = result.unique().scalar_one()
            added_service_detail = ServiceDetailDTO.model_validate(model, from_attributes=True)
            await self.session.commit()
            return added_service_detail
        except:
            return None
    
    async def read_all(self, service_id: int|None, detail_id: int|None):
        service_detail_list = []
        statement = select(ServiceDetail).options(joinedload(ServiceDetail.detail)).options(joinedload(ServiceDetail.service))
        if service_id:
            statement = statement.filter(ServiceDetail.service_id == service_id)

        if detail_id:
            statement = statement.filter(ServiceDetail.detail_id == detail_id)

        result = await self.session.execute(statement)
        service_detail = result.scalars().all()
        for row in service_detail:
            service_detail_list.append(ServiceDetailRelDTO.model_validate(row, from_attributes=True))
        if not service_detail_list:
            return None
        return service_detail_list

    async def read_all_rel(self):
        service_detail_list = []
        statement = select(ServiceDetail).options(joinedload(ServiceDetail.detail)).options(joinedload(ServiceDetail.service))
        result = await self.session.execute(statement)
        service_detail = result.scalars().all()
        for row in service_detail:
            service_detail_list.append(ServiceDetailRelDTO.model_validate(row, from_attributes=True))
        return service_detail_list
    
    async def read_by_id(self, id: int):
        statement = select(ServiceDetail).filter(ServiceDetail.service_detail_id == id).options(joinedload(ServiceDetail.detail)).options(joinedload(ServiceDetail.service))
        result = await self.session.execute(statement)
        model = result.scalars().one_or_none()
        if model:
            return ServiceDetailRelDTO.model_validate(model, from_attributes=True)
        return None
    
    async def read_by_id_rel(self, id: int):
        statement = select(ServiceDetail).filter(ServiceDetail.service_detail_id == id).options(joinedload(ServiceDetail.detail)).options(joinedload(ServiceDetail.service))
        result = await self.session.execute(statement)
        master = result.scalars().all()
        return ServiceDetailRelDTO.model_validate(master, from_attributes=True)
    
    async def update(self, id: int, new_service_detail: ServiceDetailInDTO):
        statement = select(ServiceDetail).filter(ServiceDetail.service_detail_id == id)
        result = await self.session.execute(statement)
        changed_service_detail = result.scalar_one()
        changed_service_detail.service_id = new_service_detail.service_id
        changed_service_detail.detail_id = new_service_detail.detail_id
        await self.session.commit()
        return ServiceDetailDTO.model_validate(changed_service_detail, from_attributes=True)
    
    async def delete(self, id: int):
        deleted_service_detail = await self.session.get(ServiceDetail, id)
        await self.session.delete(deleted_service_detail)
        await self.session.commit()
        return