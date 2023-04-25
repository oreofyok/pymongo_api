from fastapi import FastAPI
from pymongo import MongoClient
from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient("localhost:27017")

db = client["cleaningstore"]
collection = db["Cluster()"]

class students(BaseModel):
    id:int
    name:str
    age:int
    gpa:float
    

app = FastAPI()

t = collection.find().sort("age",-1).limit(1)
for i in t:
    print(i)

@app.get("/items/{item_id}")
async def read_items(item_id:int):
    finder = collection.find_one({"_id":item_id})
    if finder:
        return finder
    else:
        return {"Error":"Not Found"}
    
@app.get("/max/{what}/{limit}")
async def most_what(what,limit:int):
    max = collection.find().sort(what,-1).limit(limit)
    the_max = [m for m in max]
    return {"Max":what,"Item":the_max}

@app.get("/min/{what}/{limit}")
async def min_what(what,limit:int):
    min = collection.find().sort(what,1).limit(limit)
    the_min = [m for m in min]
    return {"Min":what,"Item":the_min}
        
@app.get("/all")
async def read_all():
    finder = collection.find()
    fins = [i for i in finder]
    
    return fins

@app.post("/insert")
async def insert(ss:students):
    sid = ss.id  
    sname = ss.name 
    sage = ss.age 
    sgpa = ss.gpa 
    
    collection.insert_one({"_id":sid,"name":sname,"age":sage,"gpa":sgpa})
    found = collection.find_one({"_id":sid})
    return {"Success":sid,"item":found}

@app.delete("/delete/{item_id}")
async def delete(item_id:int):
    finder = collection.find_one({"_id":item_id})
    if finder:
        collection.delete_one({"_id":item_id})
        return {"Deleted":item_id}
    else:
        return {"Error":"not found"}
    