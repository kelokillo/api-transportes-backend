-- Crear base de datos
CREATE DATABASE evaluacion_backend_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Crear usuario
CREATE USER 'usuario_backend'@'localhost' IDENTIFIED BY 'password_backend_123';

-- Asignar permisos
GRANT ALL PRIVILEGES ON evaluacion_backend_db.* TO 'usuario_backend'@'localhost';
FLUSH PRIVILEGES;