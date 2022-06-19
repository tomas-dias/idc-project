import sys
import pandas as pd
import numpy as np
from joblib import dump, load

def main(argv):

    data = argv.split(",")
    type = data[0]
    voltage_battery = float(data[1])
    current_battery = float(data[2])
    temp_battery = float(data[3])
    current_load = float(data[4])
    voltage_load = float(data[5])

    ModelC = load('charge-predictor.joblib')

    arr = []
    arr.append(voltage_battery)
    arr.append(current_battery)
    arr.append(temp_battery)
    arr.append(current_load)
    arr.append(voltage_load)

    DataSetC = []
    DataSetC = [arr]
    YhatC = ModelC.predict(DataSetC)

    print(YhatC)

if __name__ == "__main__": 
    main(sys.argv[1])