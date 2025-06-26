from datetime import datetime, UTC, date
from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class HistorialDiagnostico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha:datetime = Field(default_factory=lambda: datetime.now(UTC))
    user_id:int=Field(foreign_key="user.id")
    diagnostico_id: int=Field(foreign_key="diagnostico.id")

#historial diagnostico request

class HistorialDiagnosticoRequest(BaseModel):
    user_id:int
    diagnostico_id: int

class HistorialDiagnosticoInfo(BaseModel):
    id:int
    fecha:date
    hora:str
    diagnosis_id:int
    diagnosis_name:str
    diagnosis_url_image:str
