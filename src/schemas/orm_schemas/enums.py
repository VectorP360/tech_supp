from enum import Enum

class OrderStatus(Enum):
    WIP = "WIP"
    completed = "completed"
    denied = "denied"

class ServiceType(Enum):
    replace = "replace"
    repair = "repair"
    maintance = "maintance"

class MasterStatus(Enum):
    free = "free"
    busy = "busy"

class Properties(Enum):
    manager = "manager"
    analyst = "analist"
    tech_spec = "tech_spec"