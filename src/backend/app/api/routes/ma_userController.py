from app.models.DAO.MaUserRepository import MaUserRepository
from app.models.DTO.ma_user_model import MA_USER_SELECT
from fastapi import APIRouter,Depends
from app.services.authentication import JWTService

router = APIRouter()

# MA_USERに登録されいる全件を取得する。
@router.get("/allusers")
async def get_all_users(current_user: MA_USER_SELECT = Depends(JWTService.Analysis_ACCESS_Token)):

    all_ma_userdata = MaUserRepository.get_all_user_data()

    return all_ma_userdata

# 指定されたusercdのデータを取得する。
router.get("/user/{usercd}")
async def getbyusercd(usercd:str):

    getbyusercd = MaUserRepository.getbyusercd(usercd)

    return getbyusercd