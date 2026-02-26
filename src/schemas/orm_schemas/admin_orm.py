from sqlalchemy.orm import Mapped, mapped_column

from . import intpk
from src.enums import Properties
from src.database import Base

class Admin(Base):
    __tablename__ = "admin"

    admin_id: Mapped[intpk]
    login: Mapped[str]
    password: Mapped[str]
    properties: Mapped[Properties]