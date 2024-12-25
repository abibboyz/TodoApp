from fastapi import FastAPI, Depends, HTTPException, Path
from typing import Annotated
from sqlalchemy.orm import Session
from . import models
from .models import Todos
from TodoApp.database import engine, get_db  # This imports the 'engine' from database.py

app = FastAPI()


models.Base.metadata.create_all(bind=engine)  # This creates the tables if not already created

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}")
async def read_all(db: db_dependency, todo_id: int = Path(gt = 0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code = 404, detail = "Todo item not found")