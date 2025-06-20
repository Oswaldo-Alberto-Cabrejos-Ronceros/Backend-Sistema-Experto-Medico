from abc import ABC, abstractmethod
from typing import List
from app.models.diagnostico_model import DiagnosticoResponse

class SistemaExpertoPort(ABC):
    @abstractmethod
    def diagnosticar(self, sintomas: List[str]) -> DiagnosticoResponse:
        pass
