var query = [
    { "$group": {
        "_id": {"type" : "$type", "battery_ID": msg.payload},
        "avgTime": {"$avg": "$elapsed_time"},
        "counter" : {"$count": {}}
        }
    }
]

var newMsg = {
    payload: query 
}

return newMsg
