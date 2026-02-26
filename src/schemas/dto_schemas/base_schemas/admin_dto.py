from pydantic import BaseModel

from src.enums import Properties

class AdminInDTO(BaseModel):
    login: str
    password: str
    properties: Properties

class AdminDTO(AdminInDTO):
    admin_id: int