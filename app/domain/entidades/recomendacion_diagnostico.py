from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship



class RecomendacionDiagnostico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content:str
    diagnostico_id:int=Field(foreign_key="diagnostico.id")
#recomendacion_diagnostico request

class RecomendacionDiagnosticoRequest(BaseModel):
    content:str
    diagnostico_id: int
