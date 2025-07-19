from pydantic import BaseModel, EmailStr

from typing import List, Optional
from datetime import datetime


class User(BaseModel):
    email: EmailStr
    password: str

class UserCreate(User):
    pass

class UserLogin(User):
    pass



class AddTodo(BaseModel):
    todo: str
    is_completed: bool = False


class TodoOut(AddTodo):
    id : int
    user_id: int
    date_created : datetime

    class Config:
        orm_mode = True
    
    

class UserOut(User):
    id : int
    todos : List[TodoOut] = []

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token:str
    token_type : str


class TokenData(BaseModel):
    id : Optional[int] = None


