
CREATE TABLE caracteristica_complementaria
(
  id_caracteristica INT         NOT NULL AUTO_INCREMENT,
  nombre            VARCHAR(15) NOT NULL,
  unidad_medida     VARCHAR(7)  NOT NULL,
  PRIMARY KEY (id_caracteristica)
);

ALTER TABLE caracteristica_complementaria
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

CREATE TABLE caracteristica_mascota
(
  id_mascota        INT         NOT NULL,
  id_caracteristica INT         NOT NULL,
  valor             VARCHAR(25) NOT NULL,
  PRIMARY KEY (id_mascota, id_caracteristica)
);

CREATE TABLE mascota
(
  id_mascota      INT          NOT NULL AUTO_INCREMENT,
  nombre          VARCHAR(15)  NOT NULL,
  foto            TEXT         NOT NULL COMMENT 'url',
  fec_nacimiento  DATE         NOT NULL COMMENT 'aproximada',
  sexo            CHAR         NOT NULL COMMENT 'F: femenino - M: masculino',
  estatura        NUMERIC(3,2) NOT NULL COMMENT 'metros',
  peso            NUMERIC(5,2) NOT NULL COMMENT 'kilos',
  id_tipo_mascota INT          NOT NULL,
  id_raza         INT          NOT NULL,
  fec_ingreso     TIMESTAMP    NOT NULL,
  adoptado        BOOLEAN      NOT NULL,
  discapacidad    BOOLEAN      NOT NULL,
  PRIMARY KEY (id_mascota),
  CHECK (sexo IN ('F', 'M'))
);

ALTER TABLE mascota
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

ALTER TABLE mascota
  ADD CONSTRAINT UQ_foto UNIQUE (foto);

CREATE TABLE raza
(
  id_raza INT         NOT NULL AUTO_INCREMENT,
  nombre  VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_raza)
);

ALTER TABLE raza
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

CREATE TABLE tipo_mascota
(
  id_tipo_mascota INT         NOT NULL AUTO_INCREMENT,
  nombre          VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_tipo_mascota)
);

ALTER TABLE tipo_mascota
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

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
