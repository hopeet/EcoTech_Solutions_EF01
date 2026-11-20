from ecotech.dtos import EmpleadoDatos, DepartamentoDatos, ProyectoDatos
from ecotech.modelo.usuario import Usuario
from ecotech.modelo.empleado import Empleado
from ecotech.modelo.departamento import Departamento
from ecotech.modelo.proyecto import Proyecto
from ecotech.modelo.informe import Informe


class AdministradorRRHH(Usuario):
    """Administrador de Recursos Humanos. Hereda de Usuario."""

    def __init__(
        self,
        id_usuario: int,
        nombre_usuario: str,
        password_hash: str,
        permisos_administrativos: list[str] | None = None,
        estado: bool = True,
    ) -> None:
        super().__init__(id_usuario, nombre_usuario, password_hash, estado)
        self._permisos_administrativos = (
            list(permisos_administrativos)
            if permisos_administrativos is not None
            else [
                "CREAR_EMPLEADO",
                "EDITAR_EMPLEADO",
                "CREAR_DEPARTAMENTO",
                "EDITAR_DEPARTAMENTO",
                "ELIMINAR_DEPARTAMENTO",
                "CREAR_PROYECTO",
                "EDITAR_PROYECTO",
                "ELIMINAR_PROYECTO",
                "GENERAR_INFORME",
            ]
        )

    @property
    def permisos_administrativos(self) -> list[str]:
        return list(self._permisos_administrativos)

    def registrar_empleado(
        self,
        id_usuario: int,
        id_empleado: int,
        datos: EmpleadoDatos,
        password_hash: str,
    ) -> Empleado:
        return Empleado(
            id_usuario=id_usuario,
            nombre_usuario=datos.nombre_usuario,
            password_hash=password_hash,
            id_empleado=id_empleado,
            nombre=datos.nombre,
            direccion=datos.direccion,
            telefono=datos.telefono,
            correo=datos.correo,
            salario=datos.salario,
            fecha_inicio=datos.fecha_inicio,
        )

    def crear_departamento(self, id_departamento: int, datos: DepartamentoDatos) -> Departamento:
        return Departamento(
            id_departamento=id_departamento,
            nombre=datos.nombre,
            id_gerente=datos.id_gerente,
        )

    def crear_proyecto(self, id_proyecto: int, datos: ProyectoDatos) -> Proyecto:
        return Proyecto(
            id_proyecto=id_proyecto,
            nombre=datos.nombre,
            descripcion=datos.descripcion,
            fecha_inicio=datos.fecha_inicio,
            fecha_termino=datos.fecha_termino,
        )

    def generar_informe(self, id_informe: int, tipo: str, formato: str, datos: list[dict]) -> Informe:
        informe = Informe(id_informe=id_informe, tipo=tipo, formato=formato)
        informe.generar(datos)
        return informe

    def buscar_empleado(self, empleados: list[Empleado], criterio: str) -> list[Empleado]:
        termino = criterio.strip().lower()
        return [
            e for e in empleados
            if termino in e.nombre.lower() or termino in e.correo.lower()
        ]

    def obtener_rol(self) -> str:
        return "ADMIN_RRHH"
