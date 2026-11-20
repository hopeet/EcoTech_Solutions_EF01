import re
from ecotech.excepciones import ValidacionError


class ValidadorEntrada:
    """Valida y sanitiza entradas de usuario para evitar datos corruptos o inyecciones."""

    REGEX_CORREO = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    def sanitizar(self, texto: str) -> str:
        if not isinstance(texto, str):
            raise ValidacionError("El valor debe ser texto.")
        limpio = "".join(ch for ch in texto.strip() if ch.isprintable())
        return limpio

    def validar_correo(self, correo: str) -> str:
        limpio = self.sanitizar(correo)
        if not self.REGEX_CORREO.match(limpio):
            raise ValidacionError("Formato de correo electronico invalido.")
        return limpio.lower()

    def validar_salario(self, salario: float) -> float:
        if salario <= 0:
            raise ValidacionError("El salario debe ser mayor a cero.")
        return float(salario)

    def validar_horas(self, horas: float) -> float:
        if horas <= 0 or horas > 24:
            raise ValidacionError("Las horas trabajadas deben estar entre 0.1 y 24.")
        return float(horas)
