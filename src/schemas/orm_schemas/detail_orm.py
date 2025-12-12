from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from . import intpk
from src.database import Base
from src.schemas.orm_schemas.service_detail_orm import ServiceDetail
if TYPE_CHECKING:
    from src.schemas.orm_schemas.tech_type_orm import TechType



class Detail(Base):
    __tablename__ = "detail"

    detail_id: Mapped[intpk]
    tech_type_id: Mapped[int] = mapped_column(ForeignKey("tech_type.tech_type_id"))
    name: Mapped[str]
    cost: Mapped[int]

    service_detail: Mapped[ServiceDetail] = relationship(back_populates="detail")
    tech_type: Mapped['TechType'] = relationship(back_populates="detail")