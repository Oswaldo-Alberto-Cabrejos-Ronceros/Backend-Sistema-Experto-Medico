import logging
from app.domain.servicios.sistema_experto import SistemaExpertoPort
from app.models.diagnostico_model import DiagnosticoResponse
from pyswip import Prolog
from typing import List
from pathlib import Path
from fastapi import HTTPException

logger = logging.getLogger(__name__)

class PrologAdapter(SistemaExpertoPort):
    def __init__(self):
        self.prolog = Prolog()
        path = Path(__file__).resolve().parent / "base_conocimiento.pl"
        ruta_prolog = path.as_posix()
        print(ruta_prolog)
        if not path.exists():
            logger.error(f"Archivo Prolog no encontrado: {ruta_prolog}")
            raise FileNotFoundError(f"Archivo Prolog no encontrado: {ruta_prolog}")

        self._cargar_base_conocimiento(ruta_prolog)

    def _cargar_base_conocimiento(self, ruta: str):
        try:
            list(self.prolog.query(f"consult('{ruta}')"))
            print(f"consult('{ruta}')")
            logger.info("Base de conocimiento Prolog cargada correctamente.")
            print("¿diagnostico/1?", list(self.prolog.query("current_predicate(diagnostico/1)")))

        except Exception as e:
            logger.error(f"Error al cargar base de conocimiento Prolog: {str(e)}")
            raise RuntimeError("No se pudo cargar la base de conocimiento de Prolog") from e

    def diagnosticar(self, sintomas: List[str]) -> int:
        try:
            print(sintomas)
            if not sintomas:
                raise ValueError("Debe proporcionar al menos un síntoma")

            self._limpiar_hechos()

            for sintoma in sintomas:
                if not sintoma.isdigit():
                    print(f"Sintoma inválido: {sintoma}")
                    raise ValueError(f"Sintoma inválido: {sintoma}")
                self.prolog.assertz(f"sintoma({sintoma})")
                print(f"sintoma({sintoma})")

            resultado = list(self.prolog.query("diagnostico(D)"))

            print(resultado)
            logger.debug(f"Resultado Prolog: {resultado}")

            if resultado and isinstance(resultado[0], dict) and "D" in resultado[0]:
                enfermedad = resultado[0]["D"]
            else:
                logger.warning("No se encontró un diagnóstico válido o falta la clave 'D'")
                enfermedad = 0

            return enfermedad

        except ValueError as ve:
            logger.warning(f"Entrada inválida: {str(ve)}")
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            logger.error(f"Fallo en diagnóstico: {str(e)}")
            raise HTTPException(status_code=500, detail="Error interno durante el diagnóstico")

    def _limpiar_hechos(self):
        try:
            list(self.prolog.query("retractall(sintoma(_))"))
            logger.debug("Hechos limpiados exitosamente.")
        except Exception as e:
            logger.warning(f"No se pudo limpiar hechos: {str(e)}")

    def _recomendaciones_por_enfermedad(self, enfermedad: str) -> List[str]:
        recomendaciones = {
            "gripe": ["Tomar paracetamol", "Descansar", "Tomar líquidos"],
            "cefalea": ["Tomar ibuprofeno", "Evitar pantallas brillantes"],
            "intoxicacion": ["Beber agua", "Evitar alimentos pesados", "Consultar de urgencia"]
        }
        return recomendaciones.get(enfermedad, ["Descansar", "Consultar con un especialista"])
