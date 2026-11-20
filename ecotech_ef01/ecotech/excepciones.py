class EcoTechError(Exception):
    """Excepcion base del sistema EcoTech Solutions."""


class ValidacionError(EcoTechError):
    """Error lanzado cuando un dato de entrada no cumple las reglas."""


class AutenticacionError(EcoTechError):
    """Error en el proceso de inicio de sesion."""


class AutorizacionError(EcoTechError):
    """Error de permisos insuficientes."""


class PersistenciaError(EcoTechError):
    """Error en operaciones de base de datos."""
