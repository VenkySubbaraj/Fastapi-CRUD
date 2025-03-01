from sqlalchemy.orm import Session
from . import model, schema

def create_user(db: Session, user:schema.UserCreate):
    db_user = model.User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id:int):
    return db.query(model.User).filter(model.User.id == user_id).first()

    
def update_user(db:Session, user:schema.UserCreate):
    db_user = model.User(id=user.user_id, email=user.email, name=user.name)
    db.update(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db:Session, user_id:int):
    users = db.query(model.User).filter(model.User.id == user_id)
    db.delete(users)
    db.commit()
    db.refresh(users)
    return users