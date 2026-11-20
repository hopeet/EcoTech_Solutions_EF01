from datetime import datetime
import json


class Informe:
    """Consolida y exporta reportes del sistema."""

    def __init__(
        self,
        id_informe: int,
        tipo: str,
        formato: str = "TXT",
        fecha_generacion: datetime | None = None,
    ) -> None:
        self._id_informe = id_informe
        self._tipo = tipo
        self._formato = formato.upper()
        self._fecha_generacion = fecha_generacion or datetime.now()
        self._contenido: list[dict] = []

    @property
    def id_informe(self) -> int:
        return self._id_informe

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def formato(self) -> str:
        return self._formato

    @property
    def fecha_generacion(self) -> datetime:
        return self._fecha_generacion

    def generar(self, datos: list[dict]) -> list[dict]:
        self._contenido = list(datos)
        self._fecha_generacion = datetime.now()
        return self._contenido

    def exportar(self) -> str:
        if self._formato == "JSON":
            return json.dumps(self._contenido, ensure_ascii=False, indent=2, default=str)
        lineas = [f"=== INFORME {self._tipo.upper()} ({self._fecha_generacion.isoformat()}) ==="]
        for fila in self._contenido:
            lineas.append(" | ".join(f"{k}: {v}" for k, v in fila.items()))
        return "\n".join(lineas)
