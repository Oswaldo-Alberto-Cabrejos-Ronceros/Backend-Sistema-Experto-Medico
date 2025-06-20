from fastapi import APIRouter
from app.models.diagnostico_model import DiagnosticoRequest, DiagnosticoResponse
from app.infrastructure.prolog.prolog_adapter import PrologAdapter
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Bienvenido al Sistema Experto Médico"}


@router.post("/diagnostico", response_model=DiagnosticoResponse)
def diagnosticar(request: DiagnosticoRequest):
    try:
        logger.info(f"[POST /diagnostico] Request recibido: {request.sintomas}")
        servicio = PrologAdapter()
        respuesta = servicio.diagnosticar(request.sintomas)
        logger.info(f"[POST /diagnostico] Respuesta generada: {respuesta}")
        return respuesta
    except Exception as e:
        logger.error("Error al diagnosticar: %s", str(e))
        raise
