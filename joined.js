var query = [
    {
        $facet: {
            query1: [
                { "$match" : {"battery_ID" : msg.payload}},
                { "$group": {
                "_id": {
                    "type" : "$type"
                },
                "counter" : { "$sum" : 1},
                "avgTime": {"$avg": "$elapsed_time"},
                "standardDeviation": {"$stdDevSamp": "$elapsed_time"}
                }}
            ],
            query2: [ 
                {"$unwind" : "$temp_battery"},
                { "$match" : {"battery_ID" : msg.payload}},
                { "$group": {
                    "_id": {
                        "type" : "$type"
                    },
                    "minTempBattery" : {"$min" : "$temp_battery"},
                    "maxTempBattery" : {"$max" : "$temp_battery"},
                    "avgTempBattery" : {"$avg" : "$temp_battery"},
                    "standardDeviation" : {"$stdDevSamp": "$temp_battery"}
                }}
             ]
        }
    }
]

var newMsg = {
    payload: query 
}

return newMsg
