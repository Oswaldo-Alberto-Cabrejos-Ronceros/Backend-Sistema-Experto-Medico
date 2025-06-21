from abc import ABC, abstractmethod
from typing import Sequence

from app.domain.entidades.recomendacion_diagnostico import RecomendacionDiagnosticoRequest, RecomendacionDiagnostico


class RecomendacionDiagnosticoService(ABC):
    @abstractmethod
    def create_recomendacion_diagnostico(self,recomendacion_diagnostico:RecomendacionDiagnosticoRequest)->RecomendacionDiagnostico:
        pass
    @abstractmethod
    def get_all_recomendaciones_diagnostico(self)->Sequence[RecomendacionDiagnostico]:
        pass
    @abstractmethod
    def get_recomendacion_diagnostico_by_diagnostico_id(self, diagnostico_id:int)->Sequence[RecomendacionDiagnostico]:
        pass
