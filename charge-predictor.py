import pandas as pd
import numpy as np
from joblib import dump, load

FILE = '/home/tomasalexdias_gmail_com/idc-project/result.json'

#
# Extract relevant variables from JSON file 
#

offline_data = pd.read_json(FILE)

CycleNumber = offline_data["cycle_number"]

CycleType = offline_data["type"]

BVoltage = offline_data["voltage_battery"]
BCurrent = offline_data["current_battery"]
BTemperature = offline_data["temp_battery"]
BCurrentLoad = offline_data["current_load"]
BVoltageLoad = offline_data["voltage_load"]
CycleTime = offline_data["time"]
CycleFinalTime = offline_data["elapsed_time"]

DataSetC = np.empty((0, 7))

ModelC = load('charge-predictor.joblib')

