import sqlite3
from ecotech.excepciones import PersistenciaError


class GestorBD:
    """Gestiona la conexion oficial con SQLite y la estructura inicial de tablas."""

    def __init__(self, ruta_bd: str = "ecotech_ef01.db") -> None:
        self._ruta_bd = ruta_bd

    @property
    def ruta_bd(self) -> str:
        return self._ruta_bd

    def conectar(self) -> sqlite3.Connection:
        try:
            conn = sqlite3.connect(self._ruta_bd)
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA foreign_keys = ON;")
            return conn
        except sqlite3.Error as exc:
            raise PersistenciaError(f"Error al conectar con la base de datos: {exc}") from exc

    def probar_conexion(self) -> bool:
        try:
            with self.conectar() as conn:
                cursor = conn.execute("SELECT 1;")
                resultado = cursor.fetchone()
                return resultado is not None and resultado[0] == 1
        except PersistenciaError:
            return False

    def inicializar_esquema(self) -> None:
        sql_script = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            rol TEXT NOT NULL,
            estado INTEGER NOT NULL DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS departamentos (
            id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            id_gerente INTEGER NULL
        );

        CREATE TABLE IF NOT EXISTS empleados (
            id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER UNIQUE NOT NULL,
            id_departamento INTEGER NULL,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            salario TEXT NOT NULL,
            fecha_inicio TEXT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
            FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento) ON DELETE SET NULL
        );

        CREATE TABLE IF NOT EXISTS proyectos (
            id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_termino TEXT NULL
        );

        CREATE TABLE IF NOT EXISTS empleado_proyecto (
            id_empleado INTEGER NOT NULL,
            id_proyecto INTEGER NOT NULL,
            PRIMARY KEY (id_empleado, id_proyecto),
            FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE,
            FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS registros_tiempo (
            id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
            id_empleado INTEGER NOT NULL,
            id_proyecto INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            horas_trabajadas REAL NOT NULL,
            descripcion TEXT NOT NULL,
            FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE,
            FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto) ON DELETE CASCADE
        );
        """
        try:
            with self.conectar() as conn:
                conn.executescript(sql_script)
        except sqlite3.Error as exc:
            raise PersistenciaError(f"Error al inicializar el esquema de BD: {exc}") from exc
