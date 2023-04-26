from pydantic import BaseModel
from typing import Optional

class students(BaseModel):
    id:int
    name:str
    age:int
    gpa:float
    
class updateItem(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    gpa:Optional[float] = None