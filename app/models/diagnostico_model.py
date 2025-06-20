from pydantic import BaseModel
from typing import List

class DiagnosticoRequest(BaseModel):
    sintomas: List[str]

class DiagnosticoResponse(BaseModel):
    enfermedad: str
    recomendaciones: List[str]
