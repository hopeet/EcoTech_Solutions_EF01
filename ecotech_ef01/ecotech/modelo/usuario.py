from abc import ABC, abstractmethod


class Usuario(ABC):
    """Clase abstracta base para usuarios del sistema."""

    def __init__(
        self,
        id_usuario: int,
        nombre_usuario: str,
        password_hash: str,
        estado: bool = True,
    ) -> None:
        self._id_usuario = id_usuario
        self._nombre_usuario = nombre_usuario
        self._password_hash = password_hash
        self._estado = estado
        self._sesion_activa = False

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def nombre_usuario(self) -> str:
        return self._nombre_usuario

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @property
    def estado(self) -> bool:
        return self._estado

    @property
    def sesion_activa(self) -> bool:
        return self._sesion_activa

    def iniciar_sesion(self) -> bool:
        if not self._estado:
            return False
        self._sesion_activa = True
        return True

    def cerrar_sesion(self) -> None:
        self._sesion_activa = False

    def cambiar_password(self, nuevo_hash: str) -> None:
        self._password_hash = nuevo_hash

    @abstractmethod
    def obtener_rol(self) -> str:
        """Devuelve el rol especifico de la subclase."""
