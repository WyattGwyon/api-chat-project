from pymongo import MongoClient
from bson import json_util

client = MongoClient()
db = client.get_database("apichat")

def get_name(name):
    curs = db.apichat.find({"name":name}, {"name":1})
    return list(curs)

def insert_data(collection, data):
    curs = db[collection].insert_one(data)
    return {"_id": curs.inserted_id}

def update_data(collection, filt, data):
    curs = db[collection].update_one(filt,data)
    return {"_id": curs.inserted_id}