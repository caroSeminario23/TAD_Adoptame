INSERT INTO albergue (nombre, fec_creacion, ubicacion, celular)
VALUES 
  ('Refugio San Martín', '2020-05-15', POINT( -77.0428, -12.0464 ), '987654321'),
  ('Huellitas de Amor',  '2018-11-02', POINT( -77.0320, -12.0542 ), '912345678'),
  ('Patitas Felices',    '2021-07-30', POINT( -77.0456, -12.0489 ), '999888777');

INSERT INTO representante_albergue (nombres, apellidos, id_albergue)
VALUES
  ('Laura',   'Fernández', 1),
  ('Carlos',  'Rojas',     1),
  ('Diana',   'Morales',   2),
  ('Pedro',   'Valverde',  2),
  ('Andrea',  'Quispe',    3);

INSERT INTO servicio (nombre, endpoint_api, id_albergue)
VALUES
  ('get_mascota', 'https://api.sanmartin.org/mascotas', 1),
  ('get_mascota', 'https://api.huellitas.org/mascotas', 2),
  ('get_mascota', 'https://api.patitasfelices.org/mascotas', 3);
