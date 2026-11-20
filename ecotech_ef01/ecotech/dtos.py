from dataclasses import dataclass
from datetime import date


@dataclass
class EmpleadoDatos:
    nombre: str
    correo: str
    direccion: str
    telefono: str
    salario: float
    fecha_inicio: date
    nombre_usuario: str
    password_inicial: str


@dataclass
class DepartamentoDatos:
    nombre: str
    id_gerente: int | None = None


@dataclass
class ProyectoDatos:
    nombre: str
    descripcion: str
    fecha_inicio: date
    fecha_termino: date | None = None
