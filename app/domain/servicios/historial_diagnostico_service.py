from abc import ABC, abstractmethod

from sqlalchemy import Sequence

from app.domain.entidades.historial_diagnostico import HistorialDiagnosticoRequest, HistorialDiagnostico, \
    HistorialDiagnosticoInfo


class HistorialDiagnosticoService(ABC):
    @abstractmethod
    def create_historial_diagnostico(self,historial_diagnostico:HistorialDiagnosticoRequest)->HistorialDiagnostico:
        pass
    @abstractmethod
    def get_all_historial_diagnosticos(self)->Sequence[HistorialDiagnostico]:
        pass
    @abstractmethod
    def get_historial_by_user_id(self,user_id:int)->Sequence[HistorialDiagnostico]:
        pass
    @abstractmethod
    def get_historial_info_by_user_id(self, user_id:int)->Sequence[HistorialDiagnosticoInfo]:
        pass