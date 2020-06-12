DROP DATABASE IF EXISTS ecommerce_final;
CREATE DATABASE ecommerce_final;
USE ecommerce_final;


DROP TABLE IF EXISTS pais;
CREATE TABLE pais  (
  pais_id  INTEGER AUTO_INCREMENT,
  nombre  VARCHAR(80) NOT NULL,
  PRIMARY KEY (pais_id)
);



DROP TABLE IF EXISTS provincia;
CREATE TABLE provincia  (
  provincia_id  INTEGER AUTO_INCREMENT,
  nombre  VARCHAR(80) NOT NULL,
  pais_id  INTEGER,
  PRIMARY KEY (provincia_id),
  FOREIGN KEY (pais_id) REFERENCES pais  (pais_id)
);



DROP TABLE IF EXISTS ciudad;
CREATE TABLE ciudad  (
  ciudad_id  INTEGER AUTO_INCREMENT,
  nombre  VARCHAR(80) NOT NULL,
  provincia_id  INTEGER,
  PRIMARY KEY (ciudad_id),
  FOREIGN KEY (provincia_id) REFERENCES provincia  (provincia_id)
) ;



DROP TABLE IF EXISTS direccion;
CREATE TABLE direccion  (
  direccion_id  INTEGER AUTO_INCREMENT,
  calle  VARCHAR(80),
  altura  INTEGER,
  codigo_postal  VARCHAR(20),
  ciudad_id  INTEGER,
  PRIMARY KEY (direccion_id),
  FOREIGN KEY (ciudad_id) REFERENCES ciudad  (ciudad_id)
);


DROP TABLE IF EXISTS marca;
CREATE TABLE marca  (
  marca_id  INTEGER AUTO_INCREMENT,
  nombre  VARCHAR(80) NOT NULL,
  PRIMARY KEY (marca_id)
);



DROP TABLE IF EXISTS categoria;
CREATE TABLE categoria  (
  categoria_id  INTEGER AUTO_INCREMENT,
  nombre  VARCHAR(80) NOT NULL,
  PRIMARY KEY (categoria_id)
) ;



DROP TABLE IF EXISTS producto;
CREATE TABLE producto  (
  producto_id  INTEGER AUTO_INCREMENT,
  nombre  VARCHAR(80) NOT NULL,
  descripcion  TEXT,
  precio  FLOAT,
  stock  INTEGER,
  categoria_id  INTEGER,
  marca_id  INTEGER,
  fecha_de_publicacion  DATETIME,
  fecha_de_ultima_modificacion  DATETIME,
  PRIMARY KEY (producto_id),
  FOREIGN KEY (categoria_id) REFERENCES categoria  (categoria_id),
  FOREIGN KEY (marca_id) REFERENCES marca  (marca_id)
);


DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario  (
  usuario_id  INTEGER AUTO_INCREMENT,
  email  VARCHAR(80) NOT NULL,
  clave  VARCHAR(150),
  nombre  VARCHAR(80),
  apellido  VARCHAR(80),
  fecha_de_nacimiento  DATE,
  dni  INTEGER,
  telefono  INTEGER,
  direccion_id  INTEGER,
  fecha_de_registro  DATETIME,
  PRIMARY KEY (usuario_id),
  FOREIGN KEY (direccion_id) REFERENCES direccion  (direccion_id)
);


DROP TABLE IF EXISTS compra;
CREATE TABLE compra  (
  compra_id  INTEGER AUTO_INCREMENT,
  usuario_id  INTEGER,
  direccion_id  INTEGER,
  producto_id  INTEGER,
  cantidad  INTEGER,
  precio_total  FLOAT,
  fecha_de_compra  DATETIME,
  PRIMARY KEY (compra_id),
  FOREIGN KEY (usuario_id) REFERENCES usuario  (usuario_id),
  FOREIGN KEY (direccion_id) REFERENCES direccion  (direccion_id),
  FOREIGN KEY (producto_id) REFERENCES producto  (producto_id)
);

DROP TABLE IF EXISTS carrito;
CREATE TABLE carrito  (
  carrito_id  INTEGER AUTO_INCREMENT,
  usuario_id  INTEGER,
  producto_id  INTEGER,
  cantidad  INTEGER,
  PRIMARY KEY (carrito_id),
  FOREIGN KEY (usuario_id) REFERENCES usuario  (usuario_id),
  FOREIGN KEY (producto_id) REFERENCES producto  (producto_id)
);

INSERT INTO pais(pais_id, nombre) VALUES (2, "Argentina");
INSERT INTO pais(pais_id, nombre) VALUES (3, "Uruguay");
INSERT INTO pais(pais_id, nombre) VALUES (4, "España");
INSERT INTO pais(pais_id, nombre) VALUES (5, "Alemania");
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (2, "CABA", 2);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (3, "Santa Fe", 2);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (4, "La Pampa", 2);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (5, "Cataluña", 4);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (6, "Colonia", 3);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (7, "Montevideo", 3);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (2, "CABA", 2);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (3, "Rosario", 3);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (4, "Santa Rosa", 4);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (5, "Barcelona", 5);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (6, "Carmelo", 6);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (7, "Montevideo", 7);
INSERT INTO marca(marca_id, nombre) VALUES (1, "Desconocido");
INSERT INTO categoria(categoria_id, nombre) VALUES (1, "Desconocido");
