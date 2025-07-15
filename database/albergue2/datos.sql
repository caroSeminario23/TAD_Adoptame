-- Insertar tipos de mascota
INSERT INTO tipo_mascota (nombre) VALUES ('Perro');
INSERT INTO tipo_mascota (nombre) VALUES ('Gato');

-- Insertar razas
INSERT INTO raza (nombre) VALUES ('Labrador');
INSERT INTO raza (nombre) VALUES ('Persa');

-- Insertar mascotas
INSERT INTO mascota (
  nombre, foto, fec_nacimiento, sexo, estatura, peso,
  id_tipo_mascota, id_raza, fec_ingreso, adoptado, discapacidad
) VALUES (
  'Rocky', 'http://fotos.com/rocky.jpg', TO_DATE('2018-05-10', 'YYYY-MM-DD'),
  'M', 0.55, 22.4, 1, 1, SYSTIMESTAMP, 0, 0
);

INSERT INTO mascota (
  nombre, foto, fec_nacimiento, sexo, estatura, peso,
  id_tipo_mascota, id_raza, fec_ingreso, adoptado, discapacidad
) VALUES (
  'Luna', 'http://fotos.com/luna.jpg', TO_DATE('2020-08-25', 'YYYY-MM-DD'),
  'F', 0.25, 3.5, 2, 2, SYSTIMESTAMP, 1, 0
);

-- Insertar características complementarias
INSERT INTO caracteristica_complementaria (nombre, unidad_medida) VALUES ('Nivel de energía', 'alta');
INSERT INTO caracteristica_complementaria (nombre, unidad_medida) VALUES ('Sociabilidad', 'media');
INSERT INTO caracteristica_complementaria (nombre, unidad_medida) VALUES ('Apto niños', 'sí/no');

-- Insertar características asociadas a mascotas (por ahora asumiendo id_mascota=1 y 2, según orden de inserción)
-- Si prefieres asegurarte del ID, puedes usar una subconsulta con el nombre de la mascota

-- Para Rocky
INSERT INTO caracteristica_mascota (id_mascota, id_caracteristica, valor)
VALUES (
  (SELECT id_mascota FROM mascota WHERE nombre = 'Rocky'),
  (SELECT id_caracteristica FROM caracteristica_complementaria WHERE nombre = 'Nivel de energía'),
  'Alta'
);

-- Para Luna
INSERT INTO caracteristica_mascota (id_mascota, id_caracteristica, valor)
VALUES (
  (SELECT id_mascota FROM mascota WHERE nombre = 'Luna'),
  (SELECT id_caracteristica FROM caracteristica_complementaria WHERE nombre = 'Sociabilidad'),
  'Media'
);

-- También puedes insertar más características asociadas
INSERT INTO caracteristica_mascota (id_mascota, id_caracteristica, valor)
VALUES (
  (SELECT id_mascota FROM mascota WHERE nombre = 'Luna'),
  (SELECT id_caracteristica FROM caracteristica_complementaria WHERE nombre = 'Apto niños'),
  'Sí'
);
