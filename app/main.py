from fastapi import FastAPI
from . import models
from .database import Base, engine
from app.routers import todos, auth, user

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or replace "*" with your React URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(todos.router)
app.include_router(user.router)
app.include_router(auth.router)
