from src.schemas.dto_schemas.base_schemas.order_dto import OrderDTO
from src.schemas.dto_schemas.base_schemas.service_detail_dto import ServiceDetailDTO

from src.schemas.dto_schemas.base_schemas.service_dto import ServiceDTO

class ServiceRelDTO(ServiceDTO):
    order: list["OrderDTO"]
    service_detail: list["ServiceDetailDTO"]