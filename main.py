from fastapi import FastAPI
import model as m
import service as s

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id:int):
    return s.read_items(item_id)

@app.get("/max/{what}/{limit}")
async def most_what(what,limit:int):
    return s.most_what(what,limit)

@app.get("/min/{what}/{limit}")
async def min_what(what,limit:int):
    return s.min_what(what,limit)

@app.get("/all")
async def read_all():
    return s.read_all()

@app.post("/insert")
async def insert(ss:m.students):
    return s.insert(ss)

@app.delete("/delete/{item_id}")
async def delete(item_id:int):
    return s.delete(item_id)
