var query = [
    { "$match" : { 
        "type" :  "charge",
        "battery_ID" : msg.payload
        }
    },
    
    { "$group": {
        "avgTime": {"$avg": "$elapsed_time"},
        "counter" : {"$count": {}}
        }
    }
]

var newMsg = {
    payload: query 
}

return newMsg
