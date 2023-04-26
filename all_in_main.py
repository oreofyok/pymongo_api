from fastapi import FastAPI
from pymongo import MongoClient
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional

client = MongoClient("localhost:27017")

db = client["DBs"]
collection = db["Document"]

class students(BaseModel):
    id:int
    name:str
    age:int
    gpa:float

class updateItem(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    gpa:Optional[float] = None
    

app = FastAPI()

# found = collection.find({},{"_id"})
# F = []
# for i in found:
#     #print(i["_id"])
#     F.append(i["_id"])
# F.sort()
# L = F[-1]+1
# print(L)

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

@app.put("/change/{item_id}")
async def update_item(item_id:int,ss:updateItem):
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
        
    
@app.delete("/delete/{item_id}")
async def delete(item_id:int):
    finder = collection.find_one({"_id":item_id})
    if finder:
        collection.delete_one({"_id":item_id})
        return {"Deleted":item_id}
    else:
        return {"Error":"not found"}

@app.delete("/delete-all")
async def delete_all():
    collection.delete_many({})
    return {"Success":"All outed"}

    # found = collection.find({},{"_id"})
    
    # for i in found:
    #     print(i["_id"])
    #     collection.delete_one({"_id":i["_id"]})
    