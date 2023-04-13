from pydantic import BaseModel
from typing import Optional
from mongoengine import Document,StringField, IntField, ListField ,EmailField
from pydantic import BaseModel,EmailStr


class Book(BaseModel):
    name: str
    price: float
    author: Optional[str] = None

class User(Document):
    user_id = IntField(pk=True)
    username = StringField()
    password = StringField()
    email = EmailField()
    age = IntField()

class NewUser(BaseModel):
    user_id :int
    username : str
    password : str
    email : EmailStr
    age : int
    