from typing import TYPE_CHECKING

from pydantic import BaseModel

class TechTypeInDTO(BaseModel):
    name: str

class TechTypeDTO(TechTypeInDTO):
    tech_type_id: int