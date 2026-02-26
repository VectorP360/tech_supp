from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from . import intpk
from src.enums import OrderStatus
from src.database import Base
from src.schemas.orm_schemas.service_orm import Service
if TYPE_CHECKING:
    
    from src.schemas.orm_schemas.master_orm import Master



class Order(Base):
    __tablename__ = "order"

    order_id: Mapped[intpk]
    service_id: Mapped[int] = mapped_column(ForeignKey("service.service_id"))
    master_id: Mapped[int] = mapped_column(ForeignKey("master.master_id"))
    customer_email: Mapped[str]
    customer_addres: Mapped[str]
    order_date: Mapped[datetime]
    status: Mapped["OrderStatus"]

    service: Mapped["Service"] = relationship(back_populates="order")
    master: Mapped["Master"] = relationship(back_populates="order")