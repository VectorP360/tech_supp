from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from . import intpk

from src.database import Base
from src.schemas.orm_schemas.enums import ServiceType

if TYPE_CHECKING:
    from src.schemas.orm_schemas.order_orm import Order
    from src.schemas.orm_schemas.service_detail_orm import ServiceDetail


class Service(Base):
    __tablename__ = "service"

    service_id: Mapped[intpk]
    service_type: Mapped["ServiceType"]
    cost: Mapped[int]

    order: Mapped["Order"] = relationship(back_populates="service")
    service_detail: Mapped["ServiceDetail"] = relationship(back_populates="service")