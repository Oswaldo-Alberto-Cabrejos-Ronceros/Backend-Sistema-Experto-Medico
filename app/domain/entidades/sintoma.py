from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Sintoma(SQLModel,table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    name:str

#request

class SintomaRequest(BaseModel):
    name: str

