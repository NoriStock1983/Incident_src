from fastapi import APIRouter
from app.api.routes import ma_codeController,ma_userController
from app.api.routes.authentication import authenticationController

apirouter = APIRouter()

apirouter.include_router(authenticationController.router,prefix="/auth",tags=["authenticate"])
apirouter.include_router(ma_codeController.router,prefix="/codes",tags=["macode"])
apirouter.include_router(ma_userController.router,prefix="/users",tags=["mauser"])