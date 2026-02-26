from datetime import datetime

from pydantic import BaseModel

from src.enums import OrderStatus

class OrderInDTO(BaseModel):
    service_id: int
    customer_email: str
    customer_addres: str
    order_date: datetime
    status: OrderStatus
    master_id: int
    

class OrderDTO(OrderInDTO):
    order_id: int
