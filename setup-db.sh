python3 setup-db.py

mongoimport --uri "mongodb://127.0.0.1:27017/" --db "battery-cycles" --file "offline_.json"