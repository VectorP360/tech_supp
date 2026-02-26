from src.schemas.dto_schemas.base_schemas.service_dto import ServiceDTO
from src.schemas.dto_schemas.base_schemas.detail_dto import DetailDTO
from src.schemas.dto_schemas.base_schemas.service_detail_dto import ServiceDetailDTO

class ServiceDetailRelDTO(ServiceDetailDTO):
    service: "ServiceDTO"
    detail: "DetailDTO"