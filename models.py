import pandas as pd
import numpy as np
from joblib import dump, load
from sklearn.neural_network import MLPRegressor

FILE = '/home/tomasalexdias_gmail_com/idc-project/result.json'

#
# Two functions to scale and unscale vectors, to and from [0, 1]
# Not general functions to reuse elsewhere. One assumption from local code.
#

def scale(x, minv, maxv):
    return (x - minv) / maxv
    
def unscale(x, minv, maxv):
    return (x * maxv) + minv

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

# Create two variables, DataSetC and DataSetD, to store charge and discharge data.
# All the cycles will be stored.
# These will be matrices with variables in columns and one data point per row.

DataSetC = np.empty((0, 7))
DataSetD =  np.empty((0, 7))

for i in CycleNumber:

    # Check your data for potential problems (like outliers).
    # Should we leave any cycles out of the data sets?
    # plots can help.
    
    N = len(BVoltage[i])
    CType = CycleType[i]

    t = np.array(CycleTime[i]).reshape(N,1)
    Vb = np.array(BVoltage[i]).reshape(N,1)
    Ib = np.array(BCurrent[i]).reshape(N,1)
    Tb = np.array(BTemperature[i]).reshape(N,1)
    LIb = np.array(BCurrentLoad[i]).reshape(N,1)
    LVb = np.array(BVoltageLoad[i]).reshape(N,1)
    Tleft = CycleFinalTime[i] - t

    if CType == 'charge':
        DataSetC = np.vstack((DataSetC, np.block([t, Vb, Ib, Tb, LIb, LVb, Tleft])))
    else:
        DataSetD = np.vstack((DataSetD, np.block([t, Vb, Ib, Tb, LIb, LVb, Tleft])))

# The two variables have the target output in the last column.
# Should we use all other variables as inputs to the model?
# Could some inputs be redundant?


# Scale all variables to the [0, 1] interval, so the learning algorithms don't get biased
# by the different ranges of values in the variables.

for i in range(DataSetC.shape[1]):
    v = np.hstack((DataSetC[:,i], DataSetD[:,i]))
    
    VMin = v.min()
    VMax = v.max() - VMin

    DataSetC[:,i] = scale(DataSetC[:,i], VMin, VMax)
    DataSetD[:,i] = scale(DataSetD[:,i], VMin, VMax)    

# Shuffle data

Nc = DataSetC.shape[0]
DataSetC = DataSetC[np.random.permutation(Nc), :]

Nd = DataSetD.shape[0]
DataSetD = DataSetD[np.random.permutation(Nd), :]

# Break data set into training and testing data sets
# From the available data which fraction shoud be used for each?
# How many data points to effectively train the models?

TrainSetC = DataSetC[: round(Nc * 0.7), :]
TestSetC = DataSetC[round(Nc * 0.7) :, :]

TrainSetD = DataSetD[: round(Nd * 0.7), :]
TestSetD = DataSetD[round(Nd * 0.7) :, :]

# Train model for charging cycle.
# How many neurons in the first hidden layer?
# How many neurons in the second hidden layer?
# Choose appropriate values for max_iter and tol
# All these parameters and design variable affect the final result.
# Find good compromise

HiddenLayer1 = 7
HiddenLayer2 = 3
modelC = MLPRegressor((HiddenLayer1, HiddenLayer2,), verbose = True, max_iter = 200, tol = 0.0001)
modelC.fit(TrainSetC[:, : 6], TrainSetC[:, 6])

YhatC = modelC.predict(TestSetC[:, :6])

# Train model for discharging cycle.
# How many neurons in the first hidden layer?
# How many neurons in the second hidden layer?
# Choose appropriate values for max_iter and tol
# All these parameters and design variable affect the final result.
# Find good compromise

HiddenLayer1 = 7
HiddenLayer2 = 3
modelD = MLPRegressor((HiddenLayer1, HiddenLayer2,), verbose = True, max_iter = 200, tol = 0.0001)
modelD.fit(TrainSetD[:, : 6], TrainSetD[:, 6])

YhatD = modelD.predict(TestSetD[:, :6])


# Numerical validation
# Check also standard deviation

print("Average charge test abs error:",unscale(abs(TestSetC[:,6] - YhatC).mean(), VMin, VMax))
print("Average discharge test abs error:",unscale(abs(TestSetD[:,6] - YhatD).mean(), VMin, VMax))

# Save Models

dump(modelC, '/home/tomasalexdias_gmail_com/idc-project/charge-predictor.joblib')
dump(modelD, '/home/tomasalexdias_gmail_com/idc-project/discharge-predictor.joblib')
