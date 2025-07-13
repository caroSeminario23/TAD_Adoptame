-- POSTGRESQL DATABASE SCRIPT --

CREATE TABLE caracteristica_complementaria
(
  id_caracteristica int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre            varchar(15) NOT NULL UNIQUE,
  unidad_medida     varchar(7)  NOT NULL,
  PRIMARY KEY (id_caracteristica)
);

CREATE TABLE caracteristica_mascota
(
  id_mascota        int         NOT NULL,
  id_caracteristica int         NOT NULL,
  valor             varchar(25) NOT NULL,
  PRIMARY KEY (id_mascota, id_caracteristica)
);

CREATE TABLE mascota
(
  id_mascota      int          NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre          varchar(15)  NOT NULL UNIQUE,
  foto            text         NOT NULL UNIQUE,
  fec_nacimiento  date         NOT NULL,
  sexo            char         NOT NULL,
  estatura        numeric(3,2) NOT NULL,
  peso            numeric(5,2) NOT NULL,
  id_tipo_mascota int          NOT NULL,
  id_raza         int          NOT NULL,
  fec_ingreso     timestamptz  NOT NULL,
  adoptado        boolean      NOT NULL,
  discapacidad    boolean      NOT NULL,
  PRIMARY KEY (id_mascota),
  CHECK (sexo IN ('F', 'M'))
);

COMMENT ON COLUMN mascota.foto IS 'url';

COMMENT ON COLUMN mascota.fec_nacimiento IS 'aproximada';

COMMENT ON COLUMN mascota.sexo IS 'F: femenino - M: masculino';

COMMENT ON COLUMN mascota.estatura IS 'metros';

COMMENT ON COLUMN mascota.peso IS 'kilos';

CREATE TABLE raza
(
  id_raza int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre  varchar(20) NOT NULL UNIQUE,
  PRIMARY KEY (id_raza)
);

CREATE TABLE tipo_mascota
(
  id_tipo_mascota int         NOT NULL GENERATED ALWAYS AS IDENTITY,
  nombre          varchar(20) NOT NULL UNIQUE,
  PRIMARY KEY (id_tipo_mascota)
);

ALTER TABLE mascota
  ADD CONSTRAINT FK_tipo_mascota_TO_mascota
    FOREIGN KEY (id_tipo_mascota)
    REFERENCES tipo_mascota (id_tipo_mascota);

ALTER TABLE caracteristica_mascota
  ADD CONSTRAINT FK_mascota_TO_caracteristica_mascota
    FOREIGN KEY (id_mascota)
    REFERENCES mascota (id_mascota);

ALTER TABLE caracteristica_mascota
  ADD CONSTRAINT FK_caracteristica_complementaria_TO_caracteristica_mascota
    FOREIGN KEY (id_caracteristica)
    REFERENCES caracteristica_complementaria (id_caracteristica);

ALTER TABLE mascota
  ADD CONSTRAINT FK_raza_TO_mascota
    FOREIGN KEY (id_raza)
    REFERENCES raza (id_raza);
