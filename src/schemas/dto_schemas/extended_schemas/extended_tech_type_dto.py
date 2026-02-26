from src.schemas.dto_schemas.base_schemas.detail_dto import DetailDTO
from src.schemas.dto_schemas.base_schemas.tech_type_dto import TechTypeDTO

class TechTypeRelDTO(TechTypeDTO):
    detail: list["DetailDTO"]