from fastapi import FastAPI
from . import models
from .database import Base, engine
from app.routers import todos


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(todos.router)
