from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class HistorialDiagnostico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha:datetime = Field(default_factory=datetime.utcnow)
    user_id:int=Field(foreign_key="user.id")
    diagnostico_id: int=Field(foreign_key="diagnostico.id")

#historial diagnostico request

class HistorialDiagnosticoRequest(BaseModel):
    user_id:int
    diagnostico_id: int
    