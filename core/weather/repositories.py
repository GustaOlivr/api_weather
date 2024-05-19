from pymongo import MongoClient
from django.conf import settings

client = MongoClient('mongodb://localhost:27017/')
db = client['gustaney_weather']
weather_collection = db['weather']

def create_weather(data):
    return weather_collection.insert_one(data).inserted_id

def get_all_weather():
    return list(weather_collection.find())

def get_weather_by_id(weather_id):
    return weather_collection.find_one({"_id": weather_id})

def update_weather(weather_id, data):
    return weather_collection.update_one({"_id": weather_id}, {"$set": data})

def delete_weather(weather_id):
    return weather_collection.delete_one({"_id": weather_id})
