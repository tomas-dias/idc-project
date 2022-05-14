import pymongo

if __name__ == "__main__":
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["battery-cycles"]