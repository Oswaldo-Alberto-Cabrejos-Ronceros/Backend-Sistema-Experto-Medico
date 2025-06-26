from enum import Enum
from typing import Optional
from datetime import date

from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Gender(str, Enum):
    M  = "M"
    F = "F"



class User(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    names:str
    lastnames:str
    gender:Gender
    birthdate:date
    address:str
    district:str
    province:str
    department:str
    email:str
    password:str

    #para verificar password
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)

    #para hashear contraseña

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

#request

class UserRequest(BaseModel):
    names:str
    lastnames:str
    gender:Gender
    birthdate:date
    address:str
    district:str
    province:str
    department:str
    email: str
    password: str

#dto UserResponse

class UserResponse(BaseModel):
    id:int
    names:str
    lastnames:str
    gender:Gender
    birthdate:date
    address:str
    district:str
    province:str
    department:str
    email:str