from ecotech.modelo.empleado import Empleado


class Departamento:
    """Agrupa empleados mediante relacion de agregacion."""

    def __init__(
        self,
        id_departamento: int,
        nombre: str,
        id_gerente: int | None = None,
    ) -> None:
        self._id_departamento = id_departamento
        self._nombre = nombre
        self._id_gerente = id_gerente
        self._empleados: list[Empleado] = []

    @property
    def id_departamento(self) -> int:
        return self._id_departamento

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def id_gerente(self) -> int | None:
        return self._id_gerente

    def agregar_empleado(self, empleado: Empleado) -> None:
        if empleado not in self._empleados:
            self._empleados.append(empleado)
            empleado.set_departamento(self._id_departamento)

    def eliminar_empleado(self, id_empleado: int) -> None:
        for emp in list(self._empleados):
            if emp.id_empleado == id_empleado:
                self._empleados.remove(emp)
                emp.set_departamento(None)

    def asignar_gerente(self, id_gerente: int | None) -> None:
        self._id_gerente = id_gerente

    def get_empleados(self) -> list[Empleado]:
        return list(self._empleados)
