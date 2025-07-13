
CREATE TABLE albergue
(
  id_albergue  int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre       varchar(30) NOT NULL UNIQUE,
  fec_creacion date        NOT NULL,
  ubicacion    point       NOT NULL,
  celular      varchar(9)  NOT NULL UNIQUE,
  PRIMARY KEY (id_albergue)
);

COMMENT ON COLUMN albergue.ubicacion IS 'coordenadas';

CREATE TABLE representante_albergue
(
  id_representante int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombres          varchar(50) NOT NULL,
  apellidos        varchar(50) NOT NULL,
  id_albergue      int         NOT NULL,
  PRIMARY KEY (id_representante)
);

CREATE TABLE servicio
(
  id_servicio     int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre          varchar(20) NOT NULL,
  endpoint_api    text        NOT NULL UNIQUE,
  id_albergue     int         NOT NULL,
  PRIMARY KEY (id_servicio)
);

ALTER TABLE representante_albergue
  ADD CONSTRAINT FK_albergue_TO_representante_albergue
    FOREIGN KEY (id_albergue)
    REFERENCES albergue (id_albergue);

ALTER TABLE servicio
  ADD CONSTRAINT FK_albergue_TO_servicio
    FOREIGN KEY (id_albergue)
    REFERENCES albergue (id_albergue);
