from datetime import datetime

from fastapi import APIRouter, Query
import asyncio

from src.enums import OrderStatus
from src.services.order_service import OrderService
from src.database import async_session_factory

router = APIRouter(prefix="/orders", tags=["Заказы | Транзакции"])

@router.post("/new_order")
async def add(customer_email:str, customer_addres:str, service_id: int):
    async with async_session_factory() as session:
        created_order = await OrderService(session).create_order(customer_email=customer_email, customer_addres=customer_addres, service_id=service_id)
        return created_order

@router.get("")
async def get_all_orders(master_id: int|None = Query(None), 
                         customer_email: str|None = Query(None), 
                         service_id: int|None = Query(None), 
                         status: OrderStatus|None = Query(None), 
                         order_date: datetime|None = Query(None)):
    
    async with async_session_factory() as session:
        founded_orders = await OrderService(session).get_orders(master_id=master_id, 
                                                                customer_email=customer_email, 
                                                                service_id=service_id, 
                                                                status=status, 
                                                                order_date=order_date)
        return founded_orders
 
@router.get("/{id}")
async def get_orders_by_id(id: int):
    async with async_session_factory() as session:
        return await OrderService(session).get_order_by_id(id=id)

@router.put("/change_status_to_denied")
async def change_status_to_denied(id: int):
    async with async_session_factory() as session:
        return await OrderService(session).change_status(id=id, status=OrderStatus.denied)

@router.put("/change_status_to_completed")
async def change_status_to_completed(id: int):
    async with async_session_factory() as session:
        return await OrderService(session).change_status(id=id, status=OrderStatus.completed)

@router.delete("/delete_order")
async def delete_order(id: int):
    async with async_session_factory() as session:
        return await OrderService(session).delete_order(id=id)