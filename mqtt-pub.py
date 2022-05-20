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
            l = len(doc["voltage_battery"])
            for x in range(l):
                content = {}
                content.update({"battery_ID": doc["battery_ID"]})
                content.update({"cycle_number": int(key[-3:])})
                content.update({"type": doc["type"]})
                content.update({"amb_temp": doc["amb_temp"]})
                content.update({"date_time": doc["date_time"]})
                content.update({"voltage_battery": doc["voltage_battery"][x]})
                content.update({"current_battery": doc["current_battery"][x]})
                content.update({"temp_battery": doc["temp_battery"][x]})
                content.update({"current_load": doc["current_load"][x]})
                content.update({"voltage_load": doc["voltage_load"][x]})
                content.update({"timestamp": datetime.timestamp(datetime.now())})
                mqttc.publish(topic, content)
                msgs_sent += 1
                time.sleep(5)
                
        except KeyboardInterrupt:
            sys.exit()
    
    for key in keys_2:
        try:
            doc = dataset_2[key]
            l = len(doc["voltage_battery"])
            for x in range(l):
                content = {}
                content.update({"battery_ID": doc["battery_ID"]})
                content.update({"cycle_number": int(key[-3:])})
                content.update({"type": doc["type"]})
                content.update({"amb_temp": doc["amb_temp"]})
                content.update({"date_time": doc["date_time"]})
                content.update({"voltage_battery": doc["voltage_battery"][x]})
                content.update({"current_battery": doc["current_battery"][x]})
                content.update({"temp_battery": doc["temp_battery"][x]})
                content.update({"current_load": doc["current_load"][x]})
                content.update({"voltage_load": doc["voltage_load"][x]})
                content.update({"timestamp": datetime.timestamp(datetime.now())})
                mqttc.publish(topic, content)
                msgs_sent += 1
                time.sleep(5)

        except KeyboardInterrupt:
            sys.exit()
    mqttc.loop_stop()

    print("Messages sent: " + str(msgs_sent))

if __name__ == "__main__": 
    main(sys.argv[1:])
