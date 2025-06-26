from typing import Optional, List

from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


class Diagnostico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    content:str
    image_url:str

#request
class DiagnosticoRequest(BaseModel):
    name: str
    content: str
    image_url: str