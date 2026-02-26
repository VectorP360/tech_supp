from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from . import intpk
from src.database import Base
from src.schemas.orm_schemas.detail_orm import Detail

if TYPE_CHECKING:
    
    from src.schemas.orm_schemas.service_orm import Service



class ServiceDetail(Base):
    __tablename__ = "service_detail"

    service_detail_id: Mapped[intpk]
    service_id: Mapped[int] = mapped_column(ForeignKey("service.service_id"))
    detail_id: Mapped[int] = mapped_column(ForeignKey("detail.detail_id"))

    service: Mapped["Service"] = relationship(back_populates="service_detail")
    detail: Mapped["Detail"] = relationship(back_populates="service_detail")