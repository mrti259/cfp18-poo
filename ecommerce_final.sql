CREATE DATABASE  IF NOT EXISTS `ecommerce_final`;
USE `ecommerce_final`;


DROP TABLE IF EXISTS `pais`;
CREATE TABLE `pais` (
  `pais_id` INTEGER NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`pais_id`)
);

INSERT INTO `pais` VALUES (1,'Argentina'),(2,'Uruguay'),(3,'Chile'),(4,'Paraguay'),(5,'Bolivia');


DROP TABLE IF EXISTS `provincia`;
CREATE TABLE `provincia` (
  `provincia_id` INTEGER NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  `pais_id` INTEGER DEFAULT NULL,
  PRIMARY KEY (`provincia_id`),
  FOREIGN KEY (`pais_id`) REFERENCES `pais` (`pais_id`)
);

INSERT INTO `provincia` VALUES (1,'Ciudad Autónoma de Buenos Aires',1),(2,'Gran Buenos Aires',1),(3,'Buenos Aires',1),(4,'Santa Fe',1),(5,'Córdoba',1);


DROP TABLE IF EXISTS `ciudad`;
CREATE TABLE `ciudad` (
  `ciudad_id` INTEGER NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  `provincia_id` INTEGER DEFAULT NULL,
  PRIMARY KEY (`ciudad_id`),
  FOREIGN KEY (`provincia_id`) REFERENCES `provincia` (`provincia_id`)
) ;

INSERT INTO `ciudad` VALUES (1,'Ciudad Autonoma de Buenos Aires',1),(2,'Mar del Plata',3),(3,'Bahia Blanca',3),(4,'Necochea',3),(5,'San Isidro',2),(6,'Vicente Lopez',2),(7,'San Fernando',2);


DROP TABLE IF EXISTS `direccion`;
CREATE TABLE `direccion` (
  `direccion_id` INTEGER NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(80) NOT NULL,
  `altura` INTEGER NOT NULL,
  `codigo_postal` VARCHAR(20) DEFAULT NULL,
  `ciudad_id` INTEGER DEFAULT NULL,
  PRIMARY KEY (`direccion_id`),
  FOREIGN KEY (`ciudad_id`) REFERENCES `ciudad` (`ciudad_id`)
);


DROP TABLE IF EXISTS `marca`;
CREATE TABLE `marca` (
  `marca_id` INTEGER NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`marca_id`)
);

INSERT INTO `marca` VALUES (1,'Adidas'),(2,'Nike'),(3,'Reebok'),(4,'Topper'),(5,'Puma'),(6,'Converse'),(7,'Crocs'),(8,'DC'),(9,'Vans'),(10,'Le coq sportif');


DROP TABLE IF EXISTS `categoria`;
CREATE TABLE `categoria` (
  `categoria_id` INTEGER NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`categoria_id`)
) ;

INSERT INTO `categoria` VALUES (1,'Calzado y zapatillas'),(2,'Remeras'),(3,'Pantalones'),(4,'Buzos y camperas'),(5,'Pelotas'),(6,'Trajes de baño'),(7,'Ropa interior'),(8,'Otros');


DROP TABLE IF EXISTS `producto`;
CREATE TABLE `producto` (
  `producto_id` INTEGER NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(80) NOT NULL,
  `descripcion` TEXT DEFAULT NULL,
  `precio` FLOAT NOT NULL,
  `categoria_id` INTEGER DEFAULT NULL,
  `marca_id` INTEGER DEFAULT NULL,
  `fecha_de_publicacion` DATETIME NOT NULL,
  `fecha_de_ultima_modificacion` DATETIME NOT NULL,
  PRIMARY KEY (`producto_id`),
  FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`categoria_id`),
  FOREIGN KEY (`marca_id`) REFERENCES `marca` (`marca_id`)
);


DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `usuario_id` INTEGER NOT NULL AUTO_INCREMENT,
  `dni` INTEGER DEFAULT NULL,
  `nombre` VARCHAR(80) NOT NULL,
  `apellido` VARCHAR(80) NOT NULL,
  `fecha_de_nacimiento` DATE NOT NULL,
  `email` VARCHAR(80) NOT NULL,
  `clave` VARCHAR(150) NOT NULL,
  `telefono` INTEGER DEFAULT NULL,
  `direccion_id` INTEGER DEFAULT NULL,
  `fecha_de_registro` DATETIME NOT NULL,
  PRIMARY KEY (`usuario_id`),
  FOREIGN KEY (`direccion_id`) REFERENCES `direccion` (`direccion_id`)
);


DROP TABLE IF EXISTS `compra`;
CREATE TABLE `compra` (
  `compra_id` INTEGER NOT NULL AUTO_INCREMENT,
  `usuario_id` INTEGER NOT NULL,
  `direccion_id` INTEGER DEFAULT NULL,
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
  `carrito_id` INTEGER NOT NULL AUTO_INCREMENT,
  `usuario_id` INTEGER NOT NULL,
  `producto_id` INTEGER NOT NULL,
  `cantidad` INTEGER NOT NULL,
  PRIMARY KEY (`carrito_id`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`),
  FOREIGN KEY (`producto_id`) REFERENCES `producto` (`producto_id`)
);
