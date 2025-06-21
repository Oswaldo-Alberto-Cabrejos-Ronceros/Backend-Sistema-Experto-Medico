from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Diagnostico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    image_url:str

#request
class DiagnosticoRequest(BaseModel):
    name: str
    image_url: str