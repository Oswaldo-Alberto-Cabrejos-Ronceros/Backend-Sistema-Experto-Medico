import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "diagnosticos.json"

def guardar_diagnostico(data: dict):
    historico = []
    if DB_PATH.exists():
        with open(DB_PATH, "r", encoding="utf-8") as f:
            historico = json.load(f)
    historico.append(data)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=2)

def obtener_diagnosticos():
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
