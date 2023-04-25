
import model as m
from pymongo import MongoClient

client = MongoClient("localhost:27017")

db = client["cleaningstore"]
collection = db["Cluster()"]

def read_items(item_id):
    finder = collection.find_one({"_id":item_id})
    if finder:
        return finder
    else:
        return {"Error":"Not Found"}


def most_what(what,limit:int):
    max = collection.find().sort(what,-1).limit(limit)
    the_max = [m for m in max]
    return {"Max":what,"Item":the_max}

def min_what(what,limit:int):
    min = collection.find().sort(what,1).limit(limit)
    the_min = [m for m in min]
    return {"Min":what,"Item":the_min}

def read_all():
    finder = collection.find()
    fins = [i for i in finder]
    
    return fins

def insert(ss:m.students):
    sid = ss.id  
    sname = ss.name 
    sage = ss.age 
    sgpa = ss.gpa 
    
    collection.insert_one({"_id":sid,"name":sname,"age":sage,"gpa":sgpa})
    found = collection.find_one({"_id":sid})
    return {"Success":sid,"item":found}

def delete(item_id):
    finder = collection.find_one({"_id":item_id})
    if finder:
        collection.delete_one({"_id":item_id})
        return {"Deleted":item_id}
    elif finder == False:
        return {"Error":"not found"}
        
    
    