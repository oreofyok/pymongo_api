from pydantic import BaseModel

class students(BaseModel):
    id:int
    name:str
    age:int
    gpa:float