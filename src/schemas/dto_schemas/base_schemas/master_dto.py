from typing import TYPE_CHECKING

from pydantic import BaseModel

from src.enums import MasterStatus

class MasterInDTO(BaseModel):
    name: str
    phone_number: str
    status: MasterStatus

class MasterDTO(MasterInDTO):
    master_id: int
