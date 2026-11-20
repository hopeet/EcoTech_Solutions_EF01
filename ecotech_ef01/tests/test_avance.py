import os
import unittest
from datetime import date

from ecotech.dtos import EmpleadoDatos, DepartamentoDatos, ProyectoDatos
from ecotech.excepciones import ValidacionError
from ecotech.modelo.usuario import Usuario
from ecotech.modelo.administrador import AdministradorRRHH
from ecotech.servicios.autenticacion import AutenticacionServicio
from ecotech.servicios.autorizacion import AutorizacionServicio
from ecotech.servicios.validador import ValidadorEntrada
from ecotech.servicios.cifrado import CifradoServicio
from ecotech.persistencia.conexion import GestorBD


class TestAvanceEstructural(unittest.TestCase):
    def setUp(self):
        self.db_test = "test_ef01.db"
        self.auth = AutenticacionServicio()
        self.authz = AutorizacionServicio()
        self.validador = ValidadorEntrada()
        self.cifrado = CifradoServicio("clave-test")

    def tearDown(self):
        if os.path.exists(self.db_test):
            os.remove(self.db_test)

    def test_usuario_es_abstracta(self):
        with self.assertRaises(TypeError):
            Usuario(1, "user", "hash")

    def test_herencia_y_polimorfismo(self):
        admin = AdministradorRRHH(1, "admin", self.auth.hashear_password("12345678"))
        datos = EmpleadoDatos(
            nombre="Juan Perez",
            correo="juan@ecotech.cl",
            direccion="Calle 1",
            telefono="99999999",
            salario=1200000,
            fecha_inicio=date.today(),
            nombre_usuario="jperez",
            password_inicial="emp12345",
        )
        emp = admin.registrar_empleado(2, 1, datos, self.auth.hashear_password(datos.password_inicial))
        self.assertEqual(admin.obtener_rol(), "ADMIN_RRHH")
        self.assertEqual(emp.obtener_rol(), "EMPLEADO")
        self.assertTrue(self.authz.verificar_permiso(admin, "CREAR_EMPLEADO"))
        self.assertFalse(self.authz.verificar_permiso(emp, "CREAR_EMPLEADO"))

    def test_relaciones_uml(self):
        admin = AdministradorRRHH(1, "admin", "hash")
        datos = EmpleadoDatos("Ana", "ana@ecotech.cl", "Dir", "123", 1000000, date.today(), "ana", "pass")
        emp = admin.registrar_empleado(2, 1, datos, "hash2")
        depto = admin.crear_departamento(1, DepartamentoDatos("TI"))
        depto.agregar_empleado(emp)
        self.assertEqual(len(depto.get_empleados()), 1)

        proy = admin.crear_proyecto(1, ProyectoDatos("App", "Desc", date.today()))
        proy.agregar_empleado(emp)
        reg = emp.registrar_horas(1, 1, date.today(), 4.0, "Avance")
        proy.asociar_registro(reg)
        self.assertEqual(proy.consultar_horas(), 4.0)

    def test_validacion_y_cifrado(self):
        with self.assertRaises(ValidacionError):
            self.validador.validar_correo("correo-malo")
        cifrado = self.cifrado.cifrar_dato("Av. Siempre Viva 742")
        self.assertEqual(self.cifrado.descifrar_dato(cifrado), "Av. Siempre Viva 742")

    def test_conexion_bd(self):
        gestor = GestorBD(self.db_test)
        self.assertTrue(gestor.probar_conexion())
        gestor.inicializar_esquema()
        self.assertTrue(os.path.exists(self.db_test))


if __name__ == "__main__":
    unittest.main()
