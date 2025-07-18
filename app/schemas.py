from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str


class AddTodo(BaseModel):
    todo: str
    is_completed: bool
