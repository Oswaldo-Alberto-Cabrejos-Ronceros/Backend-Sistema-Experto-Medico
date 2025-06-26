from typing import List

from fastapi import APIRouter

from app.domain.entidades.historial_diagnostico import HistorialDiagnosticoRequest
from app.infrastructure.persistence.historial_diagnostico_service_impl import HistorialDiagnosticoServiceImpl
from app.models.diagnostico_model import DiagnosticoRequest, DiagnosticoResponse, DiagnosticoSessionRequest
from app.infrastructure.prolog.prolog_adapter import PrologAdapter
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

historialService= HistorialDiagnosticoServiceImpl()

@router.get("/")
def root():
    return {"message": "Bienvenido al Sistema Experto Médico"}


@router.post("/diagnostico", response_model=DiagnosticoResponse)
def diagnosticar(request: DiagnosticoRequest):
    diagnostico=ejecutar_diagnostico(request.sintomas)
    return DiagnosticoResponse(diagnostico_id=diagnostico)

@router.post("/diagnostico/session",response_model=DiagnosticoResponse)
def diagnosticar_session(request:DiagnosticoSessionRequest):
    diagnostico = ejecutar_diagnostico(request.diagnosticoRequest.sintomas)
    historial_diagnostico_request=HistorialDiagnosticoRequest(user_id=request.user_id,diagnostico_id=diagnostico)
    historialService.create_historial_diagnostico(historial_diagnostico_request)
    return DiagnosticoResponse(diagnostico_id=diagnostico)

#para ejecutar diagnostico

def ejecutar_diagnostico(sintomas:List[str])->int:
    try:
        print(sintomas)
        logger.info(f"[POST /diagnostico] Request recibido: {sintomas}")
        servicio = PrologAdapter()
        respuesta = servicio.diagnosticar(sintomas)
        logger.info(f"[POST /diagnostico] Respuesta generada: {respuesta}")
        return respuesta
    except Exception as e:
        logger.error("Error al diagnosticar: %s", str(e))
        raise
