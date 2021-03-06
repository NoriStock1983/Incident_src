from sqlalchemy import create_engine

class DBAccess():

    # DB接続処理
    def connect_database():
        
        try:
            engine = create_engine('postgresql://postgres:postgres@host.docker.internal:5436/Incident')
            #engine = create_engine('postgresql://postgres:postgrespw@host.docker.internal:49153')
            conn = engine.connect()
            
        except Exception as err:
            # 接続時にエラーとなった場合、エラーを返す。
            print("--- Failed Database Access ---")
            print(err)
        finally:
            print("Successful Database Access!")
        
        return conn


        