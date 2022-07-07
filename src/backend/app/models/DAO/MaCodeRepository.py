from typing import List
from app.models.DTO.ma_code_model import Select_MA_CODE
from app.db.dbaccess import DBAccess
from sqlalchemy.sql import text


class MaCodeRepository():
    # MA_CODEの内容を全件取得する。
    def selectallcode():

        # Databaseへのアクセス
        con = DBAccess.connect_database()
        # List型の変数を定義する。（DBから取得したデータを格納する。）
        allcodedata = List[Select_MA_CODE]
        # Listを初期化する。
        allcodedata = []

        # Queryを作成（ORMを利用せず、生SQLを実行する形としている。）
        query = text("SELECT * FROM MA_CODE;")

        try:
            rows = con.execute(query)
            for row in rows:
                allcodedata.append(row)
                print(allcodedata)
                
        except Exception as err:
            print(err)
        
        finally:
            con.close()

        return allcodedata

    # MA_CODE内で、指定のIDの値1件を取得する。
    def selectbyidcode(codeid: int):

        getbyiddata = List[Select_MA_CODE]
        getbyiddata = []
        # Databaseへアクセス
        con = DBAccess.connect_database()

        query = text("SELECT * FROM MA_CODE WHERE id = :id")
        try:
            rows = con.execute(query,**{"id": codeid})
            for row in rows:
                getbyiddata = row
                
        except Exception as err:
            print(err)
        
        finally:
            con.close()

        return getbyiddata


    # MA_CODE内で、指定のCODEの値を取得する。
    def selectbycode(code1: str):

        getbycodedata = List[Select_MA_CODE]
        getbycodedata = []
        # Databaseへアクセス
        con = DBAccess.connect_database()
        query = text("SELECT * FROM MA_CODE WHERE code_1 = :code_1")
        print(query)
        try:
            rows = con.execute(query,**{"code_1": code1})
            
            for row in rows:
                getbycodedata.append(row)
                print(getbycodedata)
                
        except Exception as err:
            print(err)
        
        finally:
            con.close()

        return getbycodedata