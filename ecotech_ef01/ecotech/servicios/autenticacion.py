import hashlib
import hmac
import os


class AutenticacionServicio:
    """Gestiona hashing seguro de contrasenas y verificacion de credenciales."""

    ITERACIONES = 310_000

    def hashear_password(self, password: str) -> str:
        sal = os.urandom(16)
        clave = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), sal, self.ITERACIONES)
        return f"{sal.hex()}:{clave.hex()}"

    def validar_password(self, password: str, password_hash: str) -> bool:
        try:
            sal_hex, clave_hex = password_hash.split(":", 1)
            sal = bytes.fromhex(sal_hex)
            esperada = bytes.fromhex(clave_hex)
        except ValueError:
            return False
        calculada = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), sal, self.ITERACIONES)
        return hmac.compare_digest(calculada, esperada)

    def autenticar(self, usuario, password: str) -> bool:
        if usuario is None or not usuario.estado:
            return False
        if self.validar_password(password, usuario.password_hash):
            return usuario.iniciar_sesion()
        return False
