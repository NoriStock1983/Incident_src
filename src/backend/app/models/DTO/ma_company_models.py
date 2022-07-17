from pydantic import BaseModel
from datetime import datetime

class MA_COMPANY_BASE(BaseModel):
    id:int
    companycd: str
    companynm: str
    companynm_short: str
    class_id:int
    status_id:int
    created_by:str
    created_date:datetime
    updated_by:str
    updated_date:datetime
    update_counter:int


class MA_COMPANY_SELECT(MA_COMPANY_BASE):
    id:int
    companycd: str
    companynm: str
    companynm_short: str
    updated_by:str
    updated_date:datetime
    update_counter:int
    class_data:list[str] = []
    status_data:list[str] = []
    
class MA_COMPANY_DROPDOWNLIST(MA_COMPANY_BASE):
    id:int
    companycd: str
    companynm_short: str

class MA_COMPANY_INSERT(MA_COMPANY_BASE):
    companycd: str
    companynm: str
    companynm_short: str
    class_id:int
    status_id:int
    created_by:str
    created_date:datetime
    updated_by:str
    updated_date:datetime
    update_counter:int


class MA_COMPANY_UPDATE(MA_COMPANY_BASE):
    id:int
    companycd: str
    companynm: str
    companynm_short: str
    class_id:int
    status_id:int
    updated_by:str
    updated_date:datetime
    update_counter:int

