from datetime import datetime

from pydantic import BaseModel

from src.schemas.orm_schemas.enums import OrderStatus
from src.schemas.dto_schemas.master_dto import MasterDTO
from src.schemas.dto_schemas.service_dto import ServiceDTO

class OrderInDTO(BaseModel):
    service_id: int
    master_id: int
    customer_email: str
    customer_addres: str
    order_date: datetime
    status: OrderStatus

class OrderDTO(OrderInDTO):
    order_id: int

class OrderRelDTO(OrderDTO):
    master: "MasterDTO"
    service: "ServiceDTO"