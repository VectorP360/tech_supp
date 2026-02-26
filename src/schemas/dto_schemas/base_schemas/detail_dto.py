from typing import TYPE_CHECKING

from pydantic import BaseModel

class DetailInDTO(BaseModel):
    tech_type_id: int
    name: str
    cost: int

class DetailDTO(DetailInDTO):
    detail_id: int