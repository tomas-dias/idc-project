var query = [
    { "$group": {
        "_id": {"type" : "$type", "battery_ID": "id"},
        "Counters": "$count"
        }
    },

    { "$group": {
        "_id": {"type" : "$type", "battery_ID": "id"},
        "avgTime": {"$avg": "$elapsed_time"}
        }
    }
]

var newMsg = {
    payload: query 
}