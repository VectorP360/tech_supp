from pydantic import BaseModel

from src.schemas.orm_schemas.enums import ServiceType
from src.schemas.dto_schemas.order_dto import OrderDTO
from src.schemas.dto_schemas.service_detail_dto import ServiceDetailDTO

class ServiceInDTO(BaseModel):
    type: ServiceType
    cost: int

class ServiceDTO(ServiceInDTO):
    service_id: int

class ServiceRelDTO(ServiceDTO):
    order: list["OrderDTO"]
    service_detail: list["ServiceDetailDTO"]