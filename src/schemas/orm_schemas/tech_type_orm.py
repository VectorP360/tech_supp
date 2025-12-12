from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from . import intpk
from src.database import Base

from src.schemas.orm_schemas.detail_orm import Detail

class TechType(Base):
    __tablename__ = "tech_type"

    tech_type_id: Mapped[intpk]
    name: Mapped[str]

    detail: Mapped[Detail] = relationship(back_populates="tech_type")