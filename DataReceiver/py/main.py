from MQTT_RCV import MQTT_RCV
from getopt import getopt
import sys 

def main(mqttTopic, tableName, verbose):
    # Create a MQTT_RCV object
    mqtt_rcv_living_room = MQTT_RCV(mqttTopic = mqttTopic, tableName = tableName, verbose = verbose)

    # Start the MQTT Client
    mqtt_rcv_living_room.start()

    # Return
    return


def usage():
    print("Usage: python3 main.py -t <mqttTopic> -n <tableName> -v")
    print("Usage: python3 main.py --topic=<mqttTopic> --name=<tableName> --verbose")
    print("Usage: python3 main.py -h")
    print("Usage: python3 main.py --help")
    sys.exit(2)


if __name__ == '__main__':

    # Get the arguments
    try:
        opts, args = getopt(sys.argv[1:], "ht:n:v", ["topic=", "name=", "verbose"])
    except getopt.GetoptError:
        usage()        
    
    # Set the default values
    mqttTopic = None
    tableName = None
    verbose = False

    # Parse the arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-t", "--topic"):
            mqttTopic = arg
        elif opt in ("-n", "--name"):
            tableName = arg
        elif opt in ("-v", "--verbose"):
            verbose = True
        else:
            usage()

    # Check if the arguments are valid
    if mqttTopic is None or tableName is None:
        usage()
    
    # Start the main function
    main(mqttTopic, tableName, verbose)