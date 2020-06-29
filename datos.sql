USE ecommerce_final;

INSERT INTO pais(pais_id, nombre) VALUES (2, "Argentina");
INSERT INTO pais(pais_id, nombre) VALUES (3, "Uruguay");
INSERT INTO pais(pais_id, nombre) VALUES (4, "España");

INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (2, "CABA", 2);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (3, "Santa Fe", 2);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (4, "La Pampa", 2);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (5, "Cataluña", 4);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (6, "Colonia", 3);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (7, "Montevideo", 3);
INSERT INTO provincia(provincia_id, nombre, pais_id) VALUES (8, "Buenos Aires", 2);

INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (2, "CABA", 2);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (3, "Rosario", 3);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (4, "Santa Rosa", 4);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (5, "Barcelona", 5);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (6, "Carmelo", 6);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (7, "Montevideo", 7);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (8, "San Isidro", 8);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (9, "Mar Del Plata", 8);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (10, "Bahia Blanca", 8);
INSERT INTO ciudad(ciudad_id, nombre, provincia_id) VALUES (11, "Tandil", 8);

INSERT INTO categoria(categoria_id, nombre) VALUES (2, "Calzado");
INSERT INTO categoria(categoria_id, nombre) VALUES (3, "Remeras");
INSERT INTO categoria(categoria_id, nombre) VALUES (4, "Pantalones");
INSERT INTO categoria(categoria_id, nombre) VALUES (5, "Abrigo");
INSERT INTO categoria(categoria_id, nombre) VALUES (6, "Deportes");
INSERT INTO categoria(categoria_id, nombre) VALUES (7, "Mochila");
INSERT INTO categoria(categoria_id, nombre) VALUES (8, "Gorra");

INSERT INTO marca(marca_id, nombre) VALUES (2, "Adidas");
INSERT INTO marca(marca_id, nombre) VALUES (3, "Nike");
INSERT INTO marca(marca_id, nombre) VALUES (4, "Reebok");
INSERT INTO marca(marca_id, nombre) VALUES (5, "Puma");
INSERT INTO marca(marca_id, nombre) VALUES (6, "Topper");

INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (2, "Camiseta Boca Junios", "", 1400, 100, 3, 3, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (3, "Camiseta River Plate", "", 1400, 100, 3, 2, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (4, "Campera Adidas", "", 6000, 100, 5, 2, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (5, "Short deportivo", "", 800, 100, 4, 5, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (6, "Pelota de futbol", "", 5000, 100, 6, 6, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (7, "Zapatillas", "", 5000, 100, 2, 2, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (8, "Remera deportiva", "", 2500, 100, 3, 3, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (9, "Mochila", "", 2500, 100, 7, 5, NOW(), NOW());
INSERT INTO producto(producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (10, "Gorra", "", 1500, 100, 8, 2, NOW(), NOW());
