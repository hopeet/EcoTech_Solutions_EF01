# EcoTech Solutions - Prototipo Estructural (EF01)

Asignatura: Programacion Orientada a Objeto Seguro (TI3021) - INACAP
Evaluacion Formativa Unidad 2: Avance Estructural del Sistema de Gestion Interna.

## Estructura del Proyecto
- `ecotech/modelo/`: Clases del diagrama UML (`Usuario` abstracta, `Empleado`, `AdministradorRRHH`, `Departamento`, `Proyecto`, `RegistroTiempo`, `Informe`).
- `ecotech/dtos.py`: Objetos de transferencia de datos (`EmpleadoDatos`, `DepartamentoDatos`, `ProyectoDatos`).
- `ecotech/servicios/`: Clases de servicio (`AutenticacionServicio`, `AutorizacionServicio`, `ValidadorEntrada`, `CifradoServicio`).
- `ecotech/persistencia/`: Conexion a base de datos SQLite (`GestorBD`) y creacion de esquema relacional.
- `tests/test_avance.py`: Pruebas unitarias de POO, relaciones UML y conexion exitosa a BD.
- `main.py`: Script de demostracion y prueba de integracion estructural.

## Ejecucion
```bash
python main.py
python -m unittest discover -s tests -t .
```
