
import model as m
from pymongo import MongoClient

client = MongoClient("localhost:27017")

db = client["DBs"]
collection = db["Document"]

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


def update_item(item_id:int,ss:m.updateItem):
    finder = collection.find_one({"_id":item_id})
    if finder: 
        if ss.name != None:
            sname = ss.name
            collection.update_one({"_id":item_id},{"$set":{"name":sname}})
        if ss.age != None:
            sage = ss.age
            collection.update_one({"_id":item_id},{"$set":{"age":sage}})
        if ss.gpa != None:
            sgpa = ss.gpa 
            collection.update_one({"_id":item_id},{"$set":{"gpa":sgpa}})
    
    finder2 = collection.find_one({"_id":item_id})
    return {"updated":finder2}


def delete(item_id):
    finder = collection.find_one({"_id":item_id})
    if finder:
        collection.delete_one({"_id":item_id})
        return {"Deleted":item_id}
    elif finder == False:
        return {"Error":"not found"}

def delete_all():
    collection.delete_many({})
    return {"Success":"All outed"}
        
    # found = collection.find({},{"_id"})
    
    # for i in found:
    #     print(i["_id"])
    #     collection.delete_one({"_id":i["_id"]})
    