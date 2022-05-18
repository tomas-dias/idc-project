var query = [
    {"$unwind" : "$temp_battery"},
    { "$match" : {
            "battery_ID" : msg.payload
        }
    },
    { "$group": {
        "_id": {
            "type" : "$type"
        },
        "minTempBattery" : {"$min" : "$temp_battery"}
        }
    }
]

var newMsg = {
    payload: query 
}

return newMsg