from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.routers import order_router, admin_router, master_router, tech_type_router, detail_router, service_router, service_detail_router

app = FastAPI()

app.include_router(order_router.router)
app.include_router(admin_router.router)
app.include_router(master_router.router)
app.include_router(tech_type_router.router)
app.include_router(detail_router.router)
app.include_router(service_router.router)
app.include_router(service_detail_router.router)