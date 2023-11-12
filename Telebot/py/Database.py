import mysql.connector as mysql
from json import load
from env import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB_NAME

class Database:
    def __init__(self):
        self.conn = mysql.connect(host     = MYSQL_HOST,  
                                  user     = MYSQL_USER, 
                                  password = MYSQL_PASSWORD,
                                  database = MYSQL_DB_NAME)

        self.lastData = {"id"            : None, 
                        "time"           : None, 
                        "temperature"    : None, 
                        "humidity"       : None, 
                        "pressure"       : None,
                        "altitude"       : None,
                        "gas_resistance" : None}

    def __del__(self):
        self.conn.close()

    def getLastData(self):
        """
        Returns the last row of the LivingRoom table
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM LivingRoom ORDER BY id DESC LIMIT 1")
        self.lastData["id"], self.lastData["time"], self.lastData["temperature"], self.lastData["humidity"], self.lastData["pressure"], self.lastData["altitude"], self.lastData["gas_resistance"] = cursor.fetchone()
        return self.lastData
    
    def getData(self, data, number = 1):
        """
        Returns the number last rows of the LivingRoom table
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT time, " + data + " FROM LivingRoom ORDER BY id DESC LIMIT " + str(number))
        listData = list(cursor.fetchall())
        self.lastData["time"] = listData[0][0]
        self.lastData[data]   = listData[0][1]
        return listData[::-1]
    

if __name__ == "__main__":
    db = Database()
    print(db.getLastData())
    print(db.getData("id", number=10))
    print(db.getData("time", number=10))
    print(db.getData("temperature", number=10))
    print(db.getData("humidity", number=10))
    print(db.getData("pressure", number=10))
