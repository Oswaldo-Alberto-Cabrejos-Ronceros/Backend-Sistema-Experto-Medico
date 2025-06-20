class Paciente:
    def __init__(self, nombre: str, edad: int, sintomas: list[str]):
        self.nombre = nombre
        self.edad = edad
        self.sintomas = sintomas

    def resumen(self) -> str:
        return f"{self.nombre} ({self.edad} años) presenta: {', '.join(self.sintomas)}"
