var query = [
    { "$match" : {
            "battery_ID" : msg.payload
        }
    },
    { "$group": {
        "_id": {
            "type" : "$type"
        },
        "avgTime": {"$avg": "$elapsed_time"},
        "counter" : { "$sum" : 1}
        }
    }
]

var newMsg = {
    payload: query 
}

return newMsg
