from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from http.client import HTTPException
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.models.DAO import MaUserRepository
from app.models.DTO.authentication.authentication_model import JWTMeta,JWTCreds,JWTPayload
from app.core import config

# 
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
# 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")

class AuthenticationService:

    # パスワードをハッシュ化する
    def hash_password(password: str):
        hashed_password = pwd_context.hash(password)

        return hashed_password

    # 入力されたPWとハッシュ化されたPWを比較する。入力されたPWがハッシュ化された内容と同様であれば、Trueを返す。
    def verify_password(password:str,hashed_password: str):
        pw_check = pwd_context.verify(password,hashed_password)

        return pw_check


class JWTService:
    # Access Tokenの生成()
    def create_access_token(usercd:str):

        jwt_meta = JWTMeta(
            iss = config.JWT_ISS,
            audience = config.JWT_AUDIENCE,
            iat = datetime.timestamp(datetime.utcnow()),
            exp=datetime.timestamp(datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINIUTES))
        )

        jwtcreds = JWTCreds(
            usercd = usercd,
            token_type = config.ACCESS_TOKEN
            )

        payload = JWTPayload(
            **jwt_meta.__dict__,
            **jwtcreds.__dict__,)

        encoded_jwt = jwt.encode(payload.__dict__,config.JWT_SECRET_KEY,algorithm=config.JWT_ALGORITHM)

        return encoded_jwt

    # Refresh Tokenの生成
    def create_refresh_token(usercd:str):

        jwt_meta = JWTMeta(
            iss = config.JWT_ISS,
            audience = config.JWT_AUDIENCE,
            iat = datetime.timestamp(datetime.utcnow()),
            exp=datetime.timestamp(datetime.utcnow() + timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINIUTES))
        )

        jwtcreds = JWTCreds(
            usercd = usercd,
            token_type = config.REFRESH_TOKEN
            )

        payload = JWTPayload(
            **jwt_meta.__dict__,
            **jwtcreds.__dict__,)

        encoded_jwt = jwt.encode(payload.__dict__,config.JWT_REFRESH_SECRET_KEY,algorithm=config.JWT_ALGORITHM)

        return encoded_jwt

    # Access Tokenの解析
    async def Analysis_ACCESS_Token(access_token:str = Depends(oauth2_scheme)):
        # エラー時の戻り値を設定

        credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
        # 設定されているAccessTokenの解析
        try:
            payload = jwt.decode(access_token,config.ACCESS_TOKEN,algorithms=config.JWT_ALGORITHM)
            usercd:str = payload.get("sub")

            print(usercd)
        except JWTError:
            raise credential_exception
        print(credential_exception)
        # AccessTokenから取得したユーザCDを使い、ユーザマスタからユーザ情報を取得する。
        user = MaUserRepository.MaUserRepository.getbyusercd(usercd)
        print(user)
        if user  is None:
            raise credential_exception

        return user

    # Refresh Tokenの解析
    def Analysis_REFRESH_Token(refresh_token:str):
        
        return False