from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

eventdb = client["eventdb"]
addevent = eventdb["addevent"]

addevent.insert_one({
    "name":"tedx",
    "venue":"bareilly",
    "date":"22 feb 2026"
})