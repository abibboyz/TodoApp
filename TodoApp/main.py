from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from . import models
from .models import Todos
from TodoApp.database import engine, get_db  # This imports the 'engine' from database.py

app = FastAPI()


models.Base.metadata.create_all(bind=engine)  # This creates the tables if not already created

@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()
