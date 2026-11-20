"""Script de verificacion estructural (EF01 - TI3021)."""
from datetime import date
from ecotech.dtos import EmpleadoDatos, DepartamentoDatos, ProyectoDatos
from ecotech.modelo.administrador import AdministradorRRHH
from ecotech.servicios.autenticacion import AutenticacionServicio
from ecotech.servicios.autorizacion import AutorizacionServicio
from ecotech.servicios.validador import ValidadorEntrada
from ecotech.servicios.cifrado import CifradoServicio
from ecotech.persistencia.conexion import GestorBD


def main() -> None:
    print("=== PRUEBA ESTRUCTURAL EF01 - ECOTECH SOLUTIONS ===")

    # 1. Servicios de seguridad
    auth = AutenticacionServicio()
    authz = AutorizacionServicio()
    validador = ValidadorEntrada()
    cifrado = CifradoServicio()

    # 2. Instanciacion de AdministradorRRHH y Empleado (Herencia desde Usuario)
    admin_hash = auth.hashear_password("AdminSeguro2026!")
    admin = AdministradorRRHH(id_usuario=1, nombre_usuario="admin.rrhh", password_hash=admin_hash)
    assert auth.autenticar(admin, "AdminSeguro2026!")
    assert authz.verificar_permiso(admin, "CREAR_EMPLEADO")

    datos_emp = EmpleadoDatos(
        nombre="Camila Rojas",
        correo=validador.validar_correo("camila.rojas@ecotech.cl"),
        direccion=cifrado.cifrar_dato("Av. Apoquindo 4500"),
        telefono=cifrado.cifrar_dato("+56987654321"),
        salario=validador.validar_salario(1850000),
        fecha_inicio=date(2026, 9, 14),
        nombre_usuario="crojas",
        password_inicial="ClaveEmp2026!",
    )
    emp_hash = auth.hashear_password(datos_emp.password_inicial)
    empleado = admin.registrar_empleado(id_usuario=2, id_empleado=10, datos=datos_emp, password_hash=emp_hash)

    # 3. Relaciones UML: Agregacion, Asociacion y Composicion
    depto = admin.crear_departamento(1, DepartamentoDatos(nombre="Ingenieria de Software", id_gerente=10))
    depto.agregar_empleado(empleado)

    proyecto = admin.crear_proyecto(
        100,
        ProyectoDatos(nombre="Portal Interno", descripcion="Migracion POO", fecha_inicio=date(2026, 9, 15)),
    )
    proyecto.agregar_empleado(empleado)

    reg = empleado.registrar_horas(1, proyecto.id_proyecto, date(2026, 9, 16), 6.5, "Implementacion de modelos")
    proyecto.asociar_registro(reg)

    print(f"[OK] Modelos y relaciones UML verificados. Horas en proyecto: {proyecto.consultar_horas()}")

    # 4. Prueba de conexion a Base de Datos (Paso 3)
    gestor = GestorBD("ecotech_ef01.db")
    assert gestor.probar_conexion(), "Fallo la conexion a la base de datos"
    gestor.inicializar_esquema()
    print(f"[OK] Conexion exitosa a base de datos SQLite: {gestor.ruta_bd}")


if __name__ == "__main__":
    main()
