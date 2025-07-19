from fastapi import FastAPI
from . import models
from .database import Base, engine
from app.routers import todos, auth, user


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(todos.router)
app.include_router(user.router)
app.include_router(auth.router)
