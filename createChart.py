def crateInput(time, battery):
    result = []
    time_length = len(time) 
    battery_length = len(battery)

    if time_length != battery_length:
        return result

    for x in time:
        result.append({"x" : time[x], "y" : battery[x]})
    
    return result

