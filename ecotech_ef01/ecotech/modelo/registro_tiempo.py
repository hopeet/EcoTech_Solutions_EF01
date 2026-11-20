from datetime import date
from ecotech.excepciones import ValidacionError


class RegistroTiempo:
    """Representa las horas trabajadas por un empleado en un proyecto."""

    def __init__(
        self,
        id_registro: int,
        id_empleado: int,
        id_proyecto: int,
        fecha: date,
        horas_trabajadas: float,
        descripcion: str,
    ) -> None:
        self._id_registro = id_registro
        self._id_empleado = id_empleado
        self._id_proyecto = id_proyecto
        self._fecha = fecha
        self._horas_trabajadas = 0.0
        self._descripcion = descripcion
        self.validar_horas(horas_trabajadas)
        self._horas_trabajadas = horas_trabajadas

    @property
    def id_registro(self) -> int:
        return self._id_registro

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def horas_trabajadas(self) -> float:
        return self._horas_trabajadas

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @staticmethod
    def validar_horas(horas: float) -> None:
        if horas <= 0 or horas > 24:
            raise ValidacionError("Las horas trabajadas deben estar entre 0.1 y 24.")

    def modificar_registro(self, nuevas_horas: float, nueva_descripcion: str) -> None:
        self.validar_horas(nuevas_horas)
        self._horas_trabajadas = nuevas_horas
        self._descripcion = nueva_descripcion
