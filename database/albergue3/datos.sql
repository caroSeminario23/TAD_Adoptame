INSERT INTO tipo_mascota (nombre) VALUES
('Perro'),
('Gato'),
('Conejo');

INSERT INTO raza (nombre) VALUES
('Labrador Retriever'),
('Persa'),
('Holland Lop');

INSERT INTO caracteristica_complementaria (nombre, unidad_medida) VALUES
('Nivel Energía', 'puntos'),
('Tamaño Orejas', 'cm'),
('Longitud Pelo', 'cm');

INSERT INTO mascota (
  nombre, foto, fec_nacimiento, sexo,
  estatura, peso, id_tipo_mascota,
  id_raza, fec_ingreso, adoptado, discapacidad
) VALUES
('Venom', 'https://micanino.com/venom.jpg', '2022-03-01', 'M', 0.55, 20.00, 1, 1, NOW(), FALSE, FALSE),
('Princesa', 'https://mimichu.com/princesa.jpg', '2020-07-15', 'F', 0.30, 4.50, 2, 2, NOW(), TRUE, FALSE),
('Copito', 'https://conejilandia.com/copito.jpg', '2023-01-20', 'M', 0.25, 1.30, 3, 3, NOW(), FALSE, TRUE);

INSERT INTO caracteristica_mascota (id_mascota, id_caracteristica, valor) VALUES
(1, 1, '80'),    -- Venom: Nivel Energía
(1, 3, '2.5'),   -- Venom: Longitud Pelo
(2, 3, '5.0'),   -- Princesa: Longitud Pelo
(3, 2, '10'),    -- Copito: Tamaño Orejas
(3, 3, '4.0');   -- Copito: Longitud Pelo
