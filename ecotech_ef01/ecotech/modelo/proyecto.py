from datetime import date
from ecotech.modelo.empleado import Empleado
from ecotech.modelo.registro_tiempo import RegistroTiempo


class Proyecto:
    """Gestiona proyectos y participacion de empleados (asociacion N:M)."""

    def __init__(
        self,
        id_proyecto: int,
        nombre: str,
        descripcion: str,
        fecha_inicio: date,
        fecha_termino: date | None = None,
    ) -> None:
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_termino = fecha_termino
        self._empleados: list[Empleado] = []
        self._registros: list[RegistroTiempo] = []

    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def fecha_inicio(self) -> date:
        return self._fecha_inicio

    @property
    def fecha_termino(self) -> date | None:
        return self._fecha_termino

    def agregar_empleado(self, empleado: Empleado) -> None:
        if empleado not in self._empleados:
            self._empleados.append(empleado)
            empleado.asignar_proyecto(self._id_proyecto)

    def quitar_empleado(self, id_empleado: int) -> None:
        self._empleados = [e for e in self._empleados if e.id_empleado != id_empleado]

    def asociar_registro(self, registro: RegistroTiempo) -> None:
        if registro.id_proyecto == self._id_proyecto and registro not in self._registros:
            self._registros.append(registro)

    def consultar_horas(self) -> float:
        return sum(r.horas_trabajadas for r in self._registros)

    def get_empleados(self) -> list[Empleado]:
        return list(self._empleados)
