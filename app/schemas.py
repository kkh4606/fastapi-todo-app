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
    owner_id: int
    date_created : datetime

    class Config:
        orm_mode = True

class UserTodoOut(AddTodo):
    id : int
    date_created : datetime
 
    class Config:
        orm_mode = True
    
    

class UserOut(BaseModel):
    id : int
    email : EmailStr
    todos : List[UserTodoOut] = []

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token:str
    token_type : str


class TokenData(BaseModel):
    id : Optional[int] = None


