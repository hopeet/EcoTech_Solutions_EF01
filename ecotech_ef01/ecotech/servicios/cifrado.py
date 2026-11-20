import base64
import hashlib
import os


class CifradoServicio:
    """Protege datos sensibles (direccion, telefono, salario)."""

    def __init__(self, clave_secreta: str | None = None) -> None:
        secreto = clave_secreta or os.getenv("ECOTECH_CLAVE", "ecotech-clave-desarrollo-ef01")
        self._clave = hashlib.sha256(secreto.encode("utf-8")).digest()

    def _xor(self, data: bytes, clave: bytes) -> bytes:
        return bytes(b ^ clave[i % len(clave)] for i, b in enumerate(data))

    def cifrar_dato(self, dato: str, clave: str | None = None) -> str:
        clave_bytes = hashlib.sha256(clave.encode("utf-8")).digest() if clave else self._clave
        cifrado = self._xor(str(dato).encode("utf-8"), clave_bytes)
        return base64.urlsafe_b64encode(cifrado).decode("ascii")

    def descifrar_dato(self, dato_cifrado: str, clave: str | None = None) -> str:
        clave_bytes = hashlib.sha256(clave.encode("utf-8")).digest() if clave else self._clave
        raw = base64.urlsafe_b64decode(dato_cifrado.encode("ascii"))
        return self._xor(raw, clave_bytes).decode("utf-8")
