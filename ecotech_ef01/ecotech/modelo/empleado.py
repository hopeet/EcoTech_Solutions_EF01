from datetime import date
from ecotech.modelo.usuario import Usuario
from ecotech.modelo.registro_tiempo import RegistroTiempo


class Empleado(Usuario):
    """Empleado de EcoTech Solutions. Hereda de Usuario."""

    def __init__(
        self,
        id_usuario: int,
        nombre_usuario: str,
        password_hash: str,
        id_empleado: int,
        nombre: str,
        direccion: str,
        telefono: str,
        correo: str,
        salario: float,
        fecha_inicio: date,
        id_departamento: int | None = None,
        estado: bool = True,
    ) -> None:
        super().__init__(id_usuario, nombre_usuario, password_hash, estado)
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._salario = salario
        self._fecha_inicio = fecha_inicio
        self._id_departamento = id_departamento
        self._proyectos_ids: list[int] = []
        self._registros_tiempo: list[RegistroTiempo] = []

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def direccion(self) -> str:
        return self._direccion

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def correo(self) -> str:
        return self._correo

    @property
    def salario(self) -> float:
        return self._salario

    @property
    def fecha_inicio(self) -> date:
        return self._fecha_inicio

    @property
    def id_departamento(self) -> int | None:
        return self._id_departamento

    @property
    def proyectos_ids(self) -> list[int]:
        return list(self._proyectos_ids)

    @property
    def registros_tiempo(self) -> list[RegistroTiempo]:
        return list(self._registros_tiempo)

    def registrar_horas(
        self,
        id_registro: int,
        id_proyecto: int,
        fecha: date,
        horas: float,
        descripcion: str,
    ) -> RegistroTiempo:
        registro = RegistroTiempo(
            id_registro=id_registro,
            id_empleado=self._id_empleado,
            id_proyecto=id_proyecto,
            fecha=fecha,
            horas_trabajadas=horas,
            descripcion=descripcion,
        )
        self._registros_tiempo.append(registro)
        return registro

    def asignar_proyecto(self, id_proyecto: int) -> None:
        if id_proyecto not in self._proyectos_ids:
            self._proyectos_ids.append(id_proyecto)

    def actualizar_datos(self, direccion: str, telefono: str, correo: str) -> None:
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo

    def actualizar_salario(self, nuevo_salario: float) -> None:
        self._salario = nuevo_salario

    def set_departamento(self, id_departamento: int | None) -> None:
        self._id_departamento = id_departamento

    def obtener_rol(self) -> str:
        return "EMPLEADO"
