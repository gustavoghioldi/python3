import requests
import sqlite3
from datetime import datetime

class Quotation:
    def __init__(self, mep:float, oficial:float, ccl:float, time_now:str)->None:
        self.__mep =  mep
        self.__oficial =  oficial
        self.__ccl =  ccl
        self.__time_now =  time_now
        
    def mep(self):
        return self.__mep
    def oficial(self):
        return self.__oficial
    def ccl(self):
        return self.__ccl
    def time_now(self):
        return self.__time_now
    
class DollarService:
    def __init__(self) -> None:
        self.url = "https://criptoya.com/api/dolar"

    def get(self)->Quotation:
        response = requests.get(self.url)
        now = datetime.now()
        return Quotation(
            response.json()["mep"], 
            response.json()["oficial"], 
            response.json()["ccl"],
            now.strftime("%Y-%m-%d:%H:%M:%S"))

class DollarDatabase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("dolar.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS dolar (mep NUMERIC, oficial NUMERIC, ccl NUMERIC, time_now TEXT)")
        
    def create(self, quotation: Quotation)->None:        
        print(f"mep: {quotation.mep()}")
        print(f"oficial: {quotation.oficial()}")
        print(f"ccl: {quotation.ccl()}")
        print(f"now: {quotation.time_now()}")
        self.cursor.execute("INSERT INTO dolar VALUES (?, ?, ?, ?)", (quotation.mep(), quotation.oficial(), quotation.ccl(), quotation.time_now()))
        self.conn.commit()
        self.conn.close()
        
if __name__ == '__main__':
    ds = DollarService()
    quotation = ds.get()
    print(quotation)
    
    dd = DollarDatabase()
    dd.create(quotation)
    