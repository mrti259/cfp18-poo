DROP DATABASE IF EXISTS `ecommerce_final`;
CREATE DATABASE `ecommerce_final`;
USE `ecommerce_final`;


DROP TABLE IF EXISTS `pais`;
CREATE TABLE `pais` (
  `pais_id` INTEGER AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`pais_id`)
);



DROP TABLE IF EXISTS `provincia`;
CREATE TABLE `provincia` (
  `provincia_id` INTEGER AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  `pais_id` INTEGER DEFAULT 0,
  PRIMARY KEY (`provincia_id`),
  FOREIGN KEY (`pais_id`) REFERENCES `pais` (`pais_id`)
);



DROP TABLE IF EXISTS `ciudad`;
CREATE TABLE `ciudad` (
  `ciudad_id` INTEGER AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  `provincia_id` INTEGER DEFAULT 0,
  PRIMARY KEY (`ciudad_id`),
  FOREIGN KEY (`provincia_id`) REFERENCES `provincia` (`provincia_id`)
) ;



DROP TABLE IF EXISTS `direccion`;
CREATE TABLE `direccion` (
  `direccion_id` INTEGER AUTO_INCREMENT,
  `calle` VARCHAR(80),
  `altura` INTEGER,
  `codigo_postal` VARCHAR(20),
  `ciudad_id` INTEGER DEFAULT 0,
  PRIMARY KEY (`direccion_id`),
  FOREIGN KEY (`ciudad_id`) REFERENCES `ciudad` (`ciudad_id`)
);


DROP TABLE IF EXISTS `marca`;
CREATE TABLE `marca` (
  `marca_id` INTEGER AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`marca_id`)
);



DROP TABLE IF EXISTS `categoria`;
CREATE TABLE `categoria` (
  `categoria_id` INTEGER AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`categoria_id`)
) ;



DROP TABLE IF EXISTS `producto`;
CREATE TABLE `producto` (
  `producto_id` INTEGER AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  `descripcion` TEXT DEFAULT NULL,
  `precio` FLOAT NOT NULL,
  `stock` INTEGER NOT NULL,
  `categoria_id` INTEGER DEFAULT 0,
  `marca_id` INTEGER DEFAULT 0,
  `fecha_de_publicacion` DATETIME NOT NULL,
  `fecha_de_ultima_modificacion` DATETIME NOT NULL,
  PRIMARY KEY (`producto_id`),
  FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`categoria_id`),
  FOREIGN KEY (`marca_id`) REFERENCES `marca` (`marca_id`)
);


DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `usuario_id` INTEGER AUTO_INCREMENT,
  `dni` INTEGER DEFAULT NULL,
  `nombre` VARCHAR(80),
  `apellido` VARCHAR(80),
  `fecha_de_nacimiento` DATE NOT NULL,
  `email` VARCHAR(80) NOT NULL,
  `clave` VARCHAR(150) NOT NULL,
  `telefono` INTEGER DEFAULT NULL,
  `direccion_id` INTEGER DEFAULT 0,
  `fecha_de_registro` DATETIME NOT NULL,
  PRIMARY KEY (`usuario_id`),
  FOREIGN KEY (`direccion_id`) REFERENCES `direccion` (`direccion_id`)
);


DROP TABLE IF EXISTS `compra`;
CREATE TABLE `compra` (
  `compra_id` INTEGER AUTO_INCREMENT,
  `usuario_id` INTEGER NOT NULL,
  `direccion_id` INTEGER NOT NULL,
  `producto_id` INTEGER NOT NULL,
  `cantidad` INTEGER NOT NULL,
  `precio_total` FLOAT NOT NULL,
  `fecha_de_compra` DATETIME NOT NULL,
  PRIMARY KEY (`compra_id`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`),
  FOREIGN KEY (`direccion_id`) REFERENCES `direccion` (`direccion_id`),
  FOREIGN KEY (`producto_id`) REFERENCES `producto` (`producto_id`)
);

DROP TABLE IF EXISTS `carrito`;
CREATE TABLE `carrito` (
  `carrito_id` INTEGER AUTO_INCREMENT,
  `usuario_id` INTEGER NOT NULL,
  `producto_id` INTEGER NOT NULL,
  `cantidad` INTEGER NOT NULL,
  PRIMARY KEY (`carrito_id`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`),
  FOREIGN KEY (`producto_id`) REFERENCES `producto` (`producto_id`)
);
