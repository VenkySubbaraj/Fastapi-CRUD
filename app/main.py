from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import model, schema, crud
from .database import SessionLocal, engine

model.base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.UserCreate)
def post_user(user:schema.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user


@app.get("/users/{user_id}", response_model=schema.User)
def get_users(user_id:int, db:Session=Depends(get_db)):
    users = crud.get_user(db,user_id=user_id)
    return users


@app.put("/users/{user_id}", response_model=schema.UserCreate)
def update_user(user_id:int, user:schema.UserCreate, db:Session=Depends(get_db)):
    users =  crud.update_user(db, user_id=user_id)
    return users


@app.delete("/users/{user_id}")
def delete_user(user_id:int, db:Session=Depends(get_db)):
    users = crud.delete_user(db, user_id=user_id)
    return users