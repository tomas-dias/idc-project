"""a simple sensor data generator that sends to an MQTT broker via paho"""
import sys
import json
import time
import paho.mqtt.client as mqtt
import os
import signal
import getopt
from datetime import datetime
import random


FILE_D1 = 'online_1.json'
FILE_D2 = 'online_2.json'

def build_dataset(file):
    f = open(file)
    return json.load(f)

# def build_time():
#     num_battery_measurements = 3492
#     time = []
#     i = 0.0

#     for _ in range(num_battery_measurements):
#         time.append(i)
#         i += random.uniform(6.0, 20.0)
    
#     return time

def signal_handler(sig, frame):
    #print('You pressed Ctrl+C.\nProgram closed.')
    sys.exit(0)


def main(argv):

    signal.signal(signal.SIGINT, signal_handler)
    
    broker = "34.163.176.8" 
    port = 1883
    topic = "battery_1"

    dataset = build_dataset(FILE_D1)
    dataset_2 = build_dataset(FILE_D2)

    keys = ["cycle_1_609", "cycle_1_611", "cycle_1_612", "cycle_1_613"]
    keys_2 = ["cycle_2_607", "cycle_2_609", "cycle_2_611", "cycle_2_612", "cycle_2_613"]

    mqttc = mqtt.Client("Publisher")
    mqttc.connect(broker, port)
    msgs_sent = 0
    mqttc.loop_start()

    for key in keys:
        try:
            doc = dataset[key]
            doc["cycle_number"] = int(key[-3:])
            #doc["time"] = build_time()
            doc["timestamp"] = datetime.timestamp(datetime.now())
            payload = json.dumps(doc)
            #print("Sending msg: " + payload)
            mqttc.publish(topic, payload)
            msgs_sent += 1
            time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()
    
    for key in keys_2:
        try:
            doc = dataset_2[key]
            doc["cycle_number"] = int(key[-3:])
            #doc["time"] = build_time()
            doc["timestamp"] = datetime.timestamp(datetime.now())
            payload = json.dumps(doc)
            #print("Sending msg: " + payload)
            mqttc.publish(topic, payload)
            msgs_sent += 1
            time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()
    mqttc.loop_stop()

    print("Messages sent: " + str(msgs_sent))

if __name__ == "__main__": 
    main(sys.argv[1:])
