var query = [
    { "$match" : {
            "battery_ID" : msg.payload
        }
    },
    { "$group": {
        "_id": {
            "type" : "$type"
        },
        "counter" : { "$sum" : 1},
        "avgTime": {"$avg": "$elapsed_time"},
        "standardDeviation": {"$stdDevSamp": "$elapsed_time"},
        "minTemperature": {"$min" : "$temp_battery"}
        }
    }
]

var newMsg = {
    payload: query 
}

return newMsg
