import json
import sys
import pandas as pd
import numpy as np
from joblib import dump, load

def main(argv):

    print(argv)
    
    # for offline_data in cursor :
    #     #
    #     # Extract relevant variables from JSON file 
    #     #

    #     print("Type " + offline_data["type"])
    #     # offline_data = pd.read_json(FILE)
    #     CycleType = offline_data["type"]
    #     BVoltage = offline_data["voltage_battery"][0]
    #     BCurrent = offline_data["current_battery"][0]
    #     BTemperature = offline_data["temp_battery"][0]
    #     BCurrentLoad = offline_data["current_load"][0]
    #     BVoltageLoad = offline_data["voltage_load"][0]
    #     #CycleTime = offline_data["time"]
    #     #CycleFinalTime = offline_data["elapsed_time"]

    #     # DataSetC = np.empty((0, 5))

    #     # Check your data for potential problems (like outliers).
    #     # Should we leave any cycles out of the data sets?
    #     # plots can help.

    #     # N = len(BVoltage)

    #     # Vb = np.array(BVoltage).reshape(N,1)
    #     # Ib = np.array(BCurrent).reshape(N,1)
    #     # Tb = np.array(BTemperature).reshape(N,1)
    #     # LIb = np.array(BCurrentLoad).reshape(N,1)
    #     # LVb = np.array(BVoltageLoad).reshape(N,1)

    #     # DataSetC = np.vstack((DataSetC, np.block([Vb, Ib, Tb, LIb, LVb])))

    #     ModelC = load('/home/tomasalexdias_gmail_com/idc-project/charge-predictor.joblib')

    #     arr = []
    #     arr.append(BVoltage)
    #     arr.append(BCurrent)
    #     arr.append(BTemperature)
    #     arr.append(BCurrentLoad)
    #     arr.append(BVoltageLoad)

    #     DataSetC = []
    #     DataSetC = [arr]
    #     YhatC = ModelC.predict(DataSetC)

    #     print(YhatC)
        
    
    #print("YhatC length: " + str(len(YhatC)))
    #print("Result length: " + str(len(result[0]["y"])))

if __name__ == "__main__": 
    main(sys.argv[1])