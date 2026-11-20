class AutorizacionServicio:
    """Control de acceso basado en roles con politica denegar por defecto."""

    MATRIZ_ROLES = {
        "ADMIN_RRHH": {
            "CREAR_EMPLEADO",
            "EDITAR_EMPLEADO",
            "CREAR_DEPARTAMENTO",
            "EDITAR_DEPARTAMENTO",
            "ELIMINAR_DEPARTAMENTO",
            "CREAR_PROYECTO",
            "EDITAR_PROYECTO",
            "ELIMINAR_PROYECTO",
            "GENERAR_INFORME",
            "REGISTRAR_HORAS",
        },
        "EMPLEADO": {
            "REGISTRAR_HORAS",
            "ACTUALIZAR_DATOS_PROPIOS",
        },
    }

    def obtener_roles(self, usuario) -> list[str]:
        if usuario is None:
            return []
        return [usuario.obtener_rol()]

    def verificar_permiso(self, usuario, permiso: str) -> bool:
        if usuario is None or not usuario.estado:
            return False
        rol = usuario.obtener_rol()
        permisos = self.MATRIZ_ROLES.get(rol, set())
        return permiso in permisos
