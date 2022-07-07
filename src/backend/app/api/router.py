
from fastapi import APIRouter
from app.api.routes import ma_codeController

apirouter = APIRouter()

apirouter.include_router(ma_codeController.router,prefix="/codes",tags=["macode"])