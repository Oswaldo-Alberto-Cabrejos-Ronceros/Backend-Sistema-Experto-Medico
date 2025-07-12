from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship



class PosiblesCausas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    c1:str
    c2:str
    c3:str
    diagnostico_id:int=Field(foreign_key="diagnostico.id")
#posibles_causas request

class PosiblesCausasRequest(BaseModel):
    c1: str
    c2: str
    c3: str
    diagnostico_id: int

