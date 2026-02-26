from pydantic import BaseModel

class ServiceDetailInDTO(BaseModel):
    service_id: int
    detail_id: int

class ServiceDetailDTO(ServiceDetailInDTO):
    service_detail_id: int
