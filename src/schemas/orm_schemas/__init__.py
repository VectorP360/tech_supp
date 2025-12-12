from typing import Annotated, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column

if TYPE_CHECKING:
    from src.schemas.orm_schemas.admin_orm import Admin
    from src.schemas.orm_schemas.detail_orm import Detail
    from src.schemas.orm_schemas.master_orm import Master
    from src.schemas.orm_schemas.order_orm import Order
    from src.schemas.orm_schemas.service_detail_orm import ServiceDetail
    from src.schemas.orm_schemas.service_orm import Service
    from src.schemas.orm_schemas.tech_type_orm import TechType

__all__ = [
    'Admin',
    'Detail',
    'Master',
    'Order',
    'ServiceDetail',
    'Service',
    'TechType'
]

intpk = Annotated[int, mapped_column(primary_key=True)]