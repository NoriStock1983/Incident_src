from app.models.DTO.ma_company_models import MA_COMPANY_DROPDOWNLIST
from pydantic import BaseModel
from datetime import datetime

class MA_USER_BASE(BaseModel):
    id: int
    usercd:str
    user_f_name:str
    user_l_name:str
    password:str
    user_mailaddress:str
    belonged_company_id:int
    belonged_dept_id:int
    auth_id:int
    status_id:int
    created_by:str
    created_date:datetime
    updated_by:str
    updated_date:datetime
    update_counter :int

class MA_USER_INSERT(MA_USER_BASE):
    usercd:str
    user_f_name:str
    user_l_name:str
    password:str
    user_mailaddress:str
    belonged_company_id:int
    belonged_dept_id:int
    auth_id:int
    status_id:int
    created_by:str
    created_date:datetime
    updated_by:str
    updated_date:datetime
    update_counter :int

class MA_USER_SELECT(BaseModel):
    usercd:str
    user_f_name:str
    user_l_name:str
    belonged_company_id:int
    belonged_dept_id:int
    auth_id:int
    updated_by:str
    updated_date:datetime
    update_counter :int

class MA_USER_UPDATE(MA_USER_BASE):
    user_f_name:str
    user_l_name:str
    user_mailaddress:str
    belonged_company_id:int
    belonged_dept_id:int
    auth_id:int
    status_id:int
    updated_by:str
    updated_date:datetime
    update_counter :int



