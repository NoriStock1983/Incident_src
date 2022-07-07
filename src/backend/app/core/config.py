from ctypes import cast
from typing import List
from pydantic import AnyHttpUrl, BaseSettings
from fastapi.config import Config
from fastapi.datastructures import Secret

config = Config(".env")

# WebAPIの情報
APP_TITLE = "IncidentManagement"
APP_VERSION = "0.0.1"
API_PRESFIX = "/api"

# DB接続情報
DB_NAME = "postgresql"
POSTGRES_SERVER = config("POSTGRES_SERVER",cast=str)
POSTGRES_USER = config("POSTGRES_USER",cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD",cast=Secret)
POSTGRES_PORT = config("POSTGRES_PORT",cast=str,default="5432")
POSTGRES_DB = config("POSTGRES_DB",cast=str)
# DB接続文字列作成
DB_ACCESS_URL = f"{DB_NAME}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_PORT}:{POSTGRES_DB}"
