from abc import ABC, abstractmethod

from sqlalchemy import Sequence

from app.domain.entidades.diagnostico import Diagnostico, DiagnosticoRequest

class DiagnosticoService(ABC):
    @abstractmethod
    def create_diagnostico(self,diagnostico:DiagnosticoRequest)->Diagnostico:
        pass

    @abstractmethod
    def get_all_diagnosticos(self)->Sequence[Diagnostico]:
        pass
