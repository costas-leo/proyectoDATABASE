CREATE DATABASE IF NOT EXISTS facturacion_telefonica;
USE facturacion_telefonica;

-- Tabla usuario
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefono VARCHAR(15) NOT NULL,
    num INT NOT NULL,
    direccion VARCHAR(255) NOT NULL
);

-- Tabla amigos
CREATE TABLE amigos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefono VARCHAR(15) NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

-- Tabla llamadas
CREATE TABLE llamadas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    duracion INT NOT NULL,
    numDeSalida VARCHAR(15) NOT NULL,
    numDeDestino VARCHAR(15) NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

-- Agregar columna 'tipo' a la tabla llamadas
ALTER TABLE llamadas
ADD COLUMN tipo ENUM('Internacional', 'Amigos', 'Nacional') NOT NULL AFTER duracion;

-- Crear tabla boleta
CREATE TABLE boleta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    fecha_generacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    costo_total DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

-- Relacionar llamadas con boletas
ALTER TABLE llamadas
ADD COLUMN boleta_id INT DEFAULT NULL,
ADD FOREIGN KEY (boleta_id) REFERENCES boleta(id) ON DELETE SET NULL;
