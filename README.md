# API REST - Gestión de Transportes

## Descripción
Este proyecto corresponde a la Evaluación N.° 2 de la asignatura Programación Backend. Consiste en una API REST desarrollada con Django REST Framework para administrar un sistema de Gestión de Transportes, permitiendo realizar operaciones CRUD completas sobre las entidades: Conductores, Vehículos y Viajes.

## Tecnologías Utilizadas
- Python
- Django 4.2
- Django REST Framework
- MariaDB (Motor de base de datos)
- Entorno Virtual (venv)

## Estructura del Proyecto
- Modelo de datos relacional.
- Serializadores para transformación de datos a JSON.
- Vistas basadas en `ModelViewSet`.
- Enrutamiento automático con `DefaultRouter`.
- Variables de entorno desacopladas (`.env`).

## Instrucciones de Instalación
1. Clonar este repositorio.
2. Crear y activar un entorno virtual (`python -m venv venv`).
3. Instalar las dependencias (`pip install -r requirements.txt`).
4. Ejecutar el script `setup_db.sql` en MariaDB para crear la base de datos y el usuario.
5. Configurar el archivo `.env` en la raíz del proyecto con las credenciales correspondientes.
6. Aplicar las migraciones: `python manage.py migrate`.
7. Iniciar el servidor local: `python manage.py runserver`.

## Endpoints Principales
Todas las operaciones CRUD (GET, POST, PUT, PATCH, DELETE) están disponibles en las siguientes rutas:
- `http://127.0.0.1:8000/api/conductores/`
- `http://127.0.0.1:8000/api/vehiculos/`
- `http://127.0.0.1:8000/api/viajes/`

## Autor
**Kalfukoyam Treuquil**  
INACAP