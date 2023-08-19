import paho.mqtt.client as mqtt
import pymysql.cursors
import sys
import json
from env import *

class MQTT_RCV():
    def __init__(self, mqttTopic, tableName, verbose = False):
        self.mqttTopic      = mqttTopic
        self.tableName      = tableName
        self.verbose        = verbose

        self.mqttBroker     = MQTT_BROKER
        self.mqttBrokerPort = MQTT_BROKER_PORT
        self.mqttUser       = MQTT_USER
        self.mqttPassword   = MQTT_PASSWORD

        self.mysqlHost      = MYSQL_HOST
        self.mysqlUser      = MYSQL_USER
        self.mysqlPassword  = MYSQL_PASSWORD
        self.tableName      = MYSQL_DB_NAME

        self.gatewayID      = GATEWAY_ID

        self.client            = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        try:
            self.client.connect(self.mqttBroker, self.mqttBrokerPort, 60)
        except:
            sys.exit("Connection to MQTT Broker failed")


    def on_connect(self, client, userdata, flags, rc):
        """
        This function is called when the MQTT Client connects to the MQTT Broker.
        """
        client.subscribe(self.mqttTopic)
        print("MQTT Client Connected")
        try:
            db = pymysql.connect(host=self.mysqlHost, user=self.mysqlUser, password=self.mysqlPassword, db=self.dbName, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            print("MySQL Client Connected to " + self.mysqlHost + " !")
            db.close()
        except:
            sys.exit("Connection to MySQL failed")


    def on_message(self, client, userdata, msg):
        """
        This function is called when a PUBLISH message is received from the MQTT Broker.
        """
        if self.verbose == True:
            print("New Transmission received !")
            print("Payload raw : ")
            print(msg.payload)
            print("\ntopic ")
            print(msg.topic)

        # Connect to the MySQL server
        db = pymysql.connect(host        = self.mysqlHost, 
                             user        = self.mysqlUser, 
                             password    = self.mysqlPassword, 
                             db          = self.dbName,
                             charset     = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
        cursor = db.cursor()
        
        # Convert the payload from a string to a dictionary
        json_dict = json.loads((msg.payload).decode("utf-8"))
        
        # Build the SQL query to insert the data into the MySQL table
        insertRequest = "INSERT INTO " + self.tableName + " (temperature, humidity) VALUES (" + str(json_dict['temperature']) + ", " + str(json_dict['humidity']) + ")"

        # Insert the data into the MySQL table
        cursor.execute(insertRequest)
        db.commit()
        
        # Close the MySQL connection
        db.close()

        if self.verbose == True:
            print('Data logged to MySQL table.')

    def start(self):
        """
        This function starts the MQTT Client.
        """
        self.client.loop_forever()
        if self.verbose == True:
            print("MQTT Client started !")


if __name__ == '__main__':

    # Create an instance of the MQTT_RCV class
    mqtt_rcv = MQTT_RCV("LivingRoom", "LivingRoom")

    # Start the MQTT Client
    mqtt_rcv.start()
