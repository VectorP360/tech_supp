from pydantic import BaseModel

from src.enums import ServiceType

class ServiceInDTO(BaseModel):
    name: str
    service_type: ServiceType
    cost: int

class ServiceDTO(ServiceInDTO):
    service_id: int