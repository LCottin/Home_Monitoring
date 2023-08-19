from MQTT_RCV import MQTT_RCV

def main(mqttTopic, tableName, verbose):
    # Create a MQTT_RCV object
    mqtt_rcv_living_room = MQTT_RCV(mqttTopic = mqttTopic, tableName = tableName, verbose = verbose)

    # Start the MQTT Client
    mqtt_rcv_living_room.start()

if __name__ == '__main__':
    main("LivingRoom", "LivingRoom", True)