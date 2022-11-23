
import configparser
import pyodbc 


 
class mssqlconnection :
        def __init__(self):
            cf = configparser.ConfigParser()
            cf.read("fmssimdata.ini")
            driver = cf.get('settings','sql_Driver')
            server = str(cf.get('settings','sql_Server'))
            username = str(cf.get('settings','username'))
            password = str(cf.get('settings','password'))
            db = str(cf.get('settings','sql_Database'))
            try:
                self.cnxn = pyodbc.connect(driver=driver, server=server, database=db,
                                        uid = username, pwd=password,)
                self.mycursor = self.cnxn.cursor()  
                
                print("SQL Server conncetion successful")
            except :
                print("SQL Server Conncetion is Failed")
        
        def getdetails(self):
            device_ids = self.mycursor.execute('EXEC GetPyUnitDetails')
            return device_ids

          

        def insert_data(self, unitno, json_string ):
            self.unino = unitno
            self.json_string = json_string
            sql_quary = """EXEC PutPyUsageData @unitno=?, @total_usage_json_string=?"""
            params = (self.unino, self.json_string)
            self.mycursor.execute(sql_quary, params)
            self.cnxn.commit()

if __name__ == "__main__":
    gg= mssqlconnection()
    tt = gg.getdetails()
    ff = gg.insert_data(73100, 'sgyjg')