from pydantic import BaseModel

from src.schemas.dto_schemas.detail_dto import DetailDTO

class TechTypeInDTO(BaseModel):
    name: str

class TechTypeDTO(TechTypeInDTO):
    tech_type_id: int

class TechTypeRelDTO(TechTypeDTO):
    detail: list["DetailDTO"]