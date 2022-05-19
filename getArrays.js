var query = [
    {"$match" : {
        "battery_ID" : msg.id,
        "cycle_number" : msg.c1
    }},
    {"$group" : {
        "time_array" : "$time",
        "current_battery" : "$current_battery"
    }}
]

var newMsg = {
    payload = query
}

return newMsg