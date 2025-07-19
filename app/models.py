from sqlalchemy import Integer, String, Column, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False, index=True)
    todos = relationship("Todo", back_populates="user")


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, nullable=False, primary_key=True)
    todo = Column(String, nullable=False)
    is_completed = Column(Boolean, nullable=False, index=True)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    user = relationship('User', back_populates='todos')
