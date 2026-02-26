from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from . import intpk
from src.enums import MasterStatus
from src.database import Base
from src.schemas.orm_schemas.order_orm import Order



class Master(Base):
    __tablename__ = "master"

    master_id: Mapped[intpk]
    name: Mapped[str]
    phone_number: Mapped[str]
    status: Mapped["MasterStatus"]

    order: Mapped[list["Order"]] = relationship(back_populates="master")