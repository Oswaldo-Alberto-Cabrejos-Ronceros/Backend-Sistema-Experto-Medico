from pydantic import BaseModel
from typing import List

class DiagnosticoRequest(BaseModel):
    sintomas: List[str]

class DiagnosticoResponse(BaseModel):
    diagnostico_id: int

class DiagnosticoSessionRequest(BaseModel):
    diagnosticoRequest:DiagnosticoRequest
    user_id:int
