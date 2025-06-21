from abc import ABC, abstractmethod
from typing import Sequence

from app.domain.entidades.sintoma import SintomaRequest, Sintoma


class SintomaService(ABC):
    @abstractmethod
    def create_sintoma(self,sintoma:SintomaRequest)->Sintoma:
        pass

    @abstractmethod
    def get_all_sintomas(self)->Sequence[Sintoma]:
        pass
