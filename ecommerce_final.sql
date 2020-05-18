CREATE DATABASE  IF NOT EXISTS `ecommerce_final`;
USE `ecommerce_final`;


DROP TABLE IF EXISTS `pais`;
CREATE TABLE `pais` (
  `pais_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`pais_id`)
);

INSERT INTO `pais` VALUES (1,'Argentina'),(2,'Uruguay'),(3,'Chile'),(4,'Paraguay'),(5,'Bolivia');


DROP TABLE IF EXISTS `provincia`;
CREATE TABLE `provincia` (
  `provincia_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `pais_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`provincia_id`),
  FOREIGN KEY (`pais_id`) REFERENCES `pais` (`pais_id`)
);

INSERT INTO `provincia` VALUES (1,'Ciudad Autónoma de Buenos Aires',1),(2,'Gran Buenos Aires',1),(3,'Buenos Aires',1),(4,'Santa Fe',1),(5,'Córdoba',1);


DROP TABLE IF EXISTS `ciudad`;
CREATE TABLE `ciudad` (
  `ciudad_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `provincia_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ciudad_id`),
  FOREIGN KEY (`provincia_id`) REFERENCES `provincia` (`provincia_id`)
) ;

INSERT INTO `ciudad` VALUES (1,'Ciudad Autonoma de Buenos Aires',1),(2,'Mar del Plata',3),(3,'Bahia Blanca',3),(4,'Necochea',3),(5,'San Isidro',2),(6,'Vicente Lopez',2),(7,'San Fernando',2);


DROP TABLE IF EXISTS `direccion`;
CREATE TABLE `direccion` (
  `direccion_id` int(11) NOT NULL AUTO_INCREMENT,
  `calle` varchar(50) NOT NULL,
  `altura` smallint(5) NOT NULL,
  `codigo_postal` smallint(4) DEFAULT NULL,
  `ciudad_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`direccion_id`),
  FOREIGN KEY (`ciudad_id`) REFERENCES `ciudad` (`ciudad_id`)
);


DROP TABLE IF EXISTS `marca`;
CREATE TABLE `marca` (
  `marca_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`marca_id`)
);

INSERT INTO `marca` VALUES (1,'Adidas'),(2,'Nike'),(3,'Reebok'),(4,'Topper'),(5,'Puma'),(6,'Converse'),(7,'Crocs'),(8,'DC'),(9,'Vans'),(10,'Le coq sportif');


DROP TABLE IF EXISTS `categoria`;
CREATE TABLE `categoria` (
  `categoria_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`categoria_id`)
) ;

INSERT INTO `categoria` VALUES (1,'Calzado y zapatillas'),(2,'Remeras'),(3,'Pantalones'),(4,'Buzos y camperas'),(5,'Pelotas'),(6,'Trajes de baño'),(7,'Ropa interior'),(8,'Otros');


DROP TABLE IF EXISTS `producto`;
CREATE TABLE `producto` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `precio` float NOT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `marca_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`producto_id`),
  FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`categoria_id`),
  FOREIGN KEY (`marca_id`) REFERENCES `marca` (`marca_id`)
);


DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `clave` char(150) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` char(20) NOT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`usuario_id`),
  FOREIGN KEY (`direccion_id`) REFERENCES `direccion` (`direccion_id`)
);


DROP TABLE IF EXISTS `compra`;
CREATE TABLE `compra` (
  `compra_id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) DEFAULT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  `producto_id` int(11) DEFAULT NULL,
  `cantidad` smallint(4) NOT NULL,
  `precio_total` float NOT NULL,
  PRIMARY KEY (`compra_id`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`),
  FOREIGN KEY (`direccion_id`) REFERENCES `direccion` (`direccion_id`),
  FOREIGN KEY (`producto_id`) REFERENCES `producto` (`producto_id`)
);
