# Sistema de Gestión de Transportes - Evaluación 3 (Backend)

Este repositorio contiene el proyecto final correspondiente a la Evaluación 3 de programación Backend (Django). Consiste en un sistema web para la gestión de transportes que integra consumo de API REST, seguridad de vistas y autenticación de usuarios.

##  Características Principales

El proyecto cumple con todos los requerimientos de la rúbrica de evaluación:

*   **API RESTful (Django Rest Framework):** Operaciones CRUD completas (GET, POST, PUT, DELETE) para la gestión de vehículos/conductores.
*   **Sistema de Autenticación:** 
    *   Formulario de Inicio y Cierre de sesión.
    *   Redirecciones automáticas para usuarios no autenticados.
*   **Vistas Protegidas:**
    *   Implementación de Vistas Basadas en Funciones (FBV) protegidas con `@login_required`.
    *   Implementación de Vistas Basadas en Clases (CBV) protegidas con `LoginRequiredMixin`.
*   **Manejo de Errores Personalizado:** Vista personalizada para errores 404 (Not Found) cuando `DEBUG=False`.
*   **Seguridad y Entorno:** Uso de archivo `.env` para ocultar credenciales de base de datos y la `SECRET_KEY` (buenas prácticas de seguridad).

##  Tecnologías Utilizadas

*   **Backend:** Python, Django, Django Rest Framework.
*   **Base de Datos:** SQL (Configuración mediante scripts).
*   **Frontend:** HTML5, CSS3 (Plantillas de Django).
*   **Control de Versiones:** Git y GitHub.

##  Instalación y Configuración Local

Si deseas correr este proyecto en tu entorno local, sigue estos pasos:

1. **Clonar el repositorio:**
   git clone https://github.com/kelokillo/api-transportes-backend.git
   cd api-transportes-backend

2. **Crear y activar el entorno virtual:**
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate

3. **Instalar las dependencias:**
   pip install -r requirements.txt

4. **Configurar las Variables de Entorno:**
   Por razones de seguridad, el archivo `.env` no se incluye en este repositorio. Debes crear un archivo `.env` en la raíz del proyecto con la siguiente estructura:
   SECRET_KEY=tu_secret_key_aqui
   DEBUG=True
   DB_NAME=nombre_base_datos
   DB_USER=usuario_bd
   DB_PASSWORD=clave_bd
   DB_HOST=localhost
   DB_PORT=3306

5. **Configurar la Base de Datos:**
   Ejecuta el script SQL adjunto en la entrega oficial (o en tu gestor de BD) para crear la base de datos, el usuario y asignar los privilegios.

6. **Aplicar migraciones e iniciar el servidor:**
   python manage.py migrate
   python manage.py runserver

##  Rutas Principales

*   `/` : Vista pública de Bienvenida.
*   `/login/` : Interfaz de inicio de sesión.
*   `/panel-fbv/` : Panel privado (Vista Basada en Funciones).
*   `/panel-cbv/` : Panel privado (Vista Basada en Clases).
*   `/api/vehiculos/` : Endpoint principal de la API REST.

---

## Autor
**Kalfukoyam Treuquil**  
INACAP
Carrera Tecnico Analista Programador