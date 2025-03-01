from pydantic import BaseModel

class UserBase(BaseModel):
    email:str
    name:str

class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    
    class config:
        orm_model = True

class UserUpdate(BaseModel):
    email:str
    name:str