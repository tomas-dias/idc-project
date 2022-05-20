import collections
import pandas as pd
import numpy as np
from joblib import dump, load
from pymongo import MongoClient

#FILE = '/home/tomasalexdias_gmail_com/idc-project/predict.json'

def main():

    client = MongoClient("127.0.0.1", 27017)
    db = client['battery-cycles']
    collection = db['online']
    cursor = collection.find({"type": "charge"})

    result = []

    for offline_data in cursor :
        #
        # Extract relevant variables from JSON file 
        #

        # offline_data = pd.read_json(FILE)
        CycleType = offline_data["type"]
        BVoltage = offline_data["voltage_battery"]
        BCurrent = offline_data["current_battery"]
        BTemperature = offline_data["temp_battery"]
        BCurrentLoad = offline_data["current_load"]
        BVoltageLoad = offline_data["voltage_load"]
        #CycleTime = offline_data["time"]
        #CycleFinalTime = offline_data["elapsed_time"]

        DataSetC = np.empty((0, 5))

        # Check your data for potential problems (like outliers).
        # Should we leave any cycles out of the data sets?
        # plots can help.

        N = len(BVoltage)

        Vb = np.array(BVoltage).reshape(N,1)
        Ib = np.array(BCurrent).reshape(N,1)
        Tb = np.array(BTemperature).reshape(N,1)
        LIb = np.array(BCurrentLoad).reshape(N,1)
        LVb = np.array(BVoltageLoad).reshape(N,1)

        DataSetC = np.vstack((DataSetC, np.block([Vb, Ib, Tb, LIb, LVb])))

        ModelC = load('charge-predictor.joblib')

        YhatC = ModelC.predict(DataSetC)

        result.append({"x": offline_data['timestamp'], "y": YhatC})
    
    return result

if __name__ == "__main__": 
    main()