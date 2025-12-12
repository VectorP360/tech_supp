from pydantic import BaseModel

from src.schemas.dto_schemas.order_dto import OrderDTO
from src.schemas.orm_schemas.enums import MasterStatus

class MasterInDTO(BaseModel):
    name: str
    phone_number: str
    status: MasterStatus

class MasterDTO(MasterInDTO):
    master_id: int

class MasterRelDTO(MasterDTO):
    order: list["OrderDTO"]