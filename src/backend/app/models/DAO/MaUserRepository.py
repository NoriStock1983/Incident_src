from typing import List
from app.models.DTO.ma_user_model import MA_USER_INSERT,MA_USER_SELECT
from app.services.authentication import JWTService
from app.db.dbaccess import DBAccess
from sqlalchemy.sql import text


class MaUserRepository():
    def get_all_user_data():
        # Databaseへのアクセス
        con = DBAccess.connect_database()
        alluserdata = List[MA_USER_INSERT]
        alluserdata = []

        # Queryを作成（ORMを利用せず、生SQLを実行する形としている。）
        query = text("SELECT * FROM MA_USER;")

        try:
            rows = con.execute(query)
            
            for row in rows:
                alluserdata.append(MA_USER_INSERT(**row))
                
        except Exception as err:
            print(err)

        finally:
            con.close()

        tokens = JWTService.create_access_token(alluserdata[0])
        print(alluserdata[0].usercd)
        print(tokens)

        return alluserdata


    # ユーザ情報取得
    def getbyusercd(usercd:str):

        getuser = List[MA_USER_SELECT]
        getuser = []
        con = DBAccess.connect_database()
        query = text("SELECT usercd,user_f_name,user_l_name,belonged_company_id,belonged_dept_id,auth_id,updated_by,updated_date,update_counter FROM MA_USER WHERE usercd = :usercd")
        print(query)
        try:
            rows = con.execute(query,**{"usercd": usercd})
            for row in rows:
                print(rows)
                getuser.append(MA_USER_SELECT(**row))

        except Exception as err:
            print(err)

        finally:
            con.close()
        print(getuser)
        return getuser

