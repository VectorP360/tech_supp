from pydantic import BaseModel

from src.schemas.dto_schemas.service_dto import ServiceDTO
from src.schemas.dto_schemas.detail_dto import DetailDTO

class ServiceDetailInDTO(BaseModel):
    service_id: int
    detail_id: int

class ServiceDetailDTO(ServiceDetailInDTO):
    service_detail_id: int

class ServiceDetailRelDTO(ServiceDetailDTO):
    service: "ServiceDTO"
    detail: "DetailDTO"