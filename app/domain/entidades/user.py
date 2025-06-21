from enum import Enum
from typing import Optional
from datetime import date

from pydantic import BaseModel
from sqlmodel import SQLModel, Field

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