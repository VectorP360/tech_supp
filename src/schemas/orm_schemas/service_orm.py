from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from . import intpk

from src.database import Base
from src.enums import ServiceType
from src.schemas.orm_schemas.service_detail_orm import ServiceDetail
if TYPE_CHECKING:
    from src.schemas.orm_schemas.order_orm import Order


class Service(Base):
    __tablename__ = "service"

    service_id: Mapped[intpk]
    name: Mapped[str]
    service_type: Mapped["ServiceType"]
    cost: Mapped[int]

    order: Mapped[list["Order"]] = relationship(back_populates="service")
    service_detail: Mapped[list["ServiceDetail"]] = relationship(back_populates="service")