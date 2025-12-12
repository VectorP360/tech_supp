from pydantic import BaseModel

from src.schemas.dto_schemas.tech_type_dto import TechTypeDTO
from src.schemas.dto_schemas.service_detail_dto import ServiceDetailDTO

class DetailInDTO(BaseModel):
    tech_type_id: int
    name: str
    cost: int

class DetailDTO(DetailInDTO):
    detail_id: int

class DetailRelDTO(DetailDTO):
    tech_type: "TechTypeDTO"
    service_detail: list["ServiceDetailDTO"]