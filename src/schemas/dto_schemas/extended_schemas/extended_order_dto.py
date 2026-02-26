from src.schemas.dto_schemas.base_schemas.master_dto import MasterDTO
from src.schemas.dto_schemas.base_schemas.service_dto import ServiceDTO
from src.schemas.dto_schemas.base_schemas.order_dto import OrderDTO

class OrderRelDTO(OrderDTO):
    master: "MasterDTO"
    service: "ServiceDTO"