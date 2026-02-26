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

class Data_search(Enum):
    creating_error = "Не получилось создать запись!"
    not_found = "Запись не найдена!"
    no_free_masters = "Нет свободных мастеров для приёма заказа!"