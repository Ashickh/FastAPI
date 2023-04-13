from fastapi import FastAPI, HTTPException, Depends,Path,Query
from models import NewUser,User
from mongoengine import connect
import json
from mongoengine.queryset.visitor import Q
from passlib.context import CryptContext


app = FastAPI()

connect(db="library_mngmnt", host="localhost", port=27017)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

@app.post("/signup")
def signup(user:NewUser):
    nw_user = User(user_id = user.user_id,
                   username = user.username,
                   password = get_password_hash(user.password),
                   email = user.email,
                   age = user.age)
    nw_user.save()
    return {"message":"New User created Succesfully","data":user}


@app.get("/users")
def get_all_users():
    users = json.loads(User.objects().to_json())
    return users

@app.get("/user/{user_id}")
def get_user(user_id: int = Path(...,gt=0)):
    user = User.objects.get(user_id=user_id)
    user_dict = {
        "user_id":user.user_id,
        "username":user.username,
        "password":user.password,
        "email": user.email,
        "age" : user.age
    }
    return user_dict
