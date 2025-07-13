INSERT INTO tipo_mascota (nombre) VALUES
('Perro'),
('Gato'),
('Conejo'),
('Ave'),
('Tortuga'),
('Hamster'),
('Pez');

INSERT INTO raza (nombre) VALUES
('Labrador'),
('Golden Retriever'),
('Persa'),
('Siames'),
('Husky'),
('Bulldog'),
('Angora'),
('Canario'),
('Pomerania'),
('Betta');

INSERT INTO caracteristica_complementaria (nombre, unidad_medida) VALUES
('Energía', 'niveles'),
('Sociabilidad', 'niveles'),
('Entrenado', 'bool'),
('Vacunado', 'bool'),
('Color', 'texto');

INSERT INTO mascota (nombre, foto, fec_nacimiento, sexo, estatura, peso, id_tipo_mascota, id_raza, fec_ingreso, adoptado, discapacidad)
VALUES
('Toby', 'url1.jpg', '2022-01-15', 'M', 0.60, 20.5, 1, 1, now(), false, false),
('Luna', 'url2.jpg', '2021-11-23', 'F', 0.35, 10.0, 2, 3, now(), true, false),
('Max', 'url3.jpg', '2023-03-10', 'M', 0.55, 25.0, 1, 2, now(), false, false),
('Mila', 'url4.jpg', '2020-09-18', 'F', 0.30, 5.5, 2, 4, now(), false, false),
('Coco', 'url5.jpg', '2021-02-07', 'M', 0.25, 2.3, 3, 7, now(), true, false),
('Rocky', 'url6.jpg', '2019-05-14', 'M', 0.70, 27.0, 1, 5, now(), false, true),
('Nala', 'url7.jpg', '2022-12-20', 'F', 0.40, 6.0, 2, 4, now(), false, false),
('Simba', 'url8.jpg', '2020-01-05', 'M', 0.45, 7.8, 2, 3, now(), true, false),
('Daisy', 'url9.jpg', '2023-04-10', 'F', 0.15, 0.8, 6, 6, now(), false, false),
('Thor', 'url10.jpg', '2021-06-11', 'M', 0.50, 21.0, 1, 1, now(), false, false),
('Bella', 'url11.jpg', '2022-08-12', 'F', 0.30, 4.3, 2, 4, now(), false, false),
('Leo', 'url12.jpg', '2020-12-01', 'M', 0.10, 0.3, 4, 8, now(), true, false),
('Milo', 'url13.jpg', '2019-03-05', 'M', 0.55, 12.0, 1, 2, now(), false, false),
('Lola', 'url14.jpg', '2022-05-23', 'F', 0.30, 5.0, 3, 7, now(), false, false),
('Zeus', 'url15.jpg', '2023-01-30', 'M', 0.20, 1.0, 5, 10, now(), false, false),
('Nina', 'url16.jpg', '2021-09-07', 'F', 0.45, 8.0, 2, 3, now(), false, true),
('Chispa', 'url17.jpg', '2022-06-16', 'F', 0.12, 0.6, 4, 8, now(), true, false),
('Tommy', 'url18.jpg', '2020-10-20', 'M', 0.33, 6.4, 1, 6, now(), false, false),
('Pepa', 'url19.jpg', '2023-02-11', 'F', 0.16, 0.5, 6, 6, now(), false, false),
('Kira', 'url20.jpg', '2022-07-25', 'F', 0.60, 23.0, 1, 1, now(), false, false);

INSERT INTO caracteristica_mascota (id_mascota, id_caracteristica, valor) VALUES
(1, 1, 'Alta'),
(1, 2, 'Media'),
(2, 3, 'true'),
(3, 4, 'true'),
(4, 5, 'Blanco y negro'),
(5, 1, 'Baja'),
(6, 3, 'false'),
(7, 2, 'Alta'),
(8, 5, 'Naranja'),
(9, 1, 'Media');
