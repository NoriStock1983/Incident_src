from app.models.DAO.MaCodeRepository import MaCodeRepository
from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer



# エンドポイントを認証によって保護する場合には、fastapi.securityのOAuth2PasswordBearerを用いる。
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

# MA_CODEに登録されいる全件を取得する。
@router.get("/all")
async def get_all_code():
    all_ma_codedata = MaCodeRepository.selectallcode()

    return all_ma_codedata

# 指定されたIDのデータを取得する。
@router.get("/getbycodeid/{id}")
async def get_by_codeid(id: int):
    getbyid_ma_code_data = MaCodeRepository.selectbyidcode(id)
    return getbyid_ma_code_data

# 指定されたCODE_1のデータを取得する。
@router.get("/getbycode/{code}")
async def get_by_code(code: str):
    getbycode_ma_code_data = MaCodeRepository.selectbycode(code)
    return getbycode_ma_code_data