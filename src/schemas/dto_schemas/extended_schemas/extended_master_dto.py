from src.schemas.dto_schemas.base_schemas.order_dto import OrderDTO  
from src.schemas.dto_schemas.base_schemas.master_dto import MasterDTO

class MasterRelDTO(MasterDTO):
    order: list["OrderDTO"]