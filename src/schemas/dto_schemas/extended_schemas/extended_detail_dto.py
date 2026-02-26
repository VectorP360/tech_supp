from src.schemas.dto_schemas.base_schemas.tech_type_dto import TechTypeDTO
from src.schemas.dto_schemas.base_schemas.service_detail_dto import ServiceDetailDTO
from src.schemas.dto_schemas.base_schemas.detail_dto import DetailDTO

class DetailTechRelDTO(DetailDTO):
    tech_type: "TechTypeDTO"

class DetailExtendedViewDTO(DetailDTO):
    tech_type_name: str

class DetailRelDTO(DetailDTO):
    tech_type: "TechTypeDTO"
    service_detail: list["ServiceDetailDTO"]