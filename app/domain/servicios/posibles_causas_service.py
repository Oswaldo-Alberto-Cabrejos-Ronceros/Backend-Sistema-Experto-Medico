from abc import ABC, abstractmethod
from typing import Sequence
from app.domain.entidades.posibles_causas import PosiblesCausas, PosiblesCausasRequest

class PosiblesCausasService(ABC):
    @abstractmethod
    def create_posibles_causas(self, posibles_causas: PosiblesCausasRequest) -> PosiblesCausas:
        pass

    @abstractmethod
    def get_all_posibles_causas(self) -> Sequence[PosiblesCausas]:
        pass

    @abstractmethod
    def get_posibles_causas_by_diagnostico_id(self, diagnostico_id: int) -> Sequence[PosiblesCausas]:
        pass
