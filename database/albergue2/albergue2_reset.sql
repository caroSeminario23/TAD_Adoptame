-- ============================
-- LIMPIEZA DE OBJETOS PREVIOS
-- ============================

-- Eliminar triggers
BEGIN EXECUTE IMMEDIATE 'DROP TRIGGER SEQ_TRG_caracteristica_complementaria'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -4080 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TRIGGER SEQ_TRG_mascota'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -4080 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TRIGGER SEQ_TRG_raza'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -4080 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TRIGGER SEQ_TRG_tipo_mascota'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -4080 THEN RAISE; END IF; END;
/

-- Eliminar secuencias
BEGIN EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_caracteristica_complementaria'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -2289 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_mascota'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -2289 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_raza'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -2289 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_tipo_mascota'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -2289 THEN RAISE; END IF; END;
/

-- Eliminar tablas
BEGIN EXECUTE IMMEDIATE 'DROP TABLE caracteristica_mascota CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE mascota CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE caracteristica_complementaria CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE raza CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;
/
BEGIN EXECUTE IMMEDIATE 'DROP TABLE tipo_mascota CASCADE CONSTRAINTS'; EXCEPTION WHEN OTHERS THEN IF SQLCODE != -942 THEN RAISE; END IF; END;
/

-- ============================
-- CREACIÓN DE OBJETOS NUEVOS
-- ============================

CREATE TABLE caracteristica_complementaria (
  id_caracteristica NUMBER(10)   NOT NULL,
  nombre            VARCHAR2(15) NOT NULL,
  unidad_medida     VARCHAR2(7)  NOT NULL,
  CONSTRAINT PK_caracteristica_complementaria PRIMARY KEY (id_caracteristica)
);

ALTER TABLE caracteristica_complementaria
  ADD CONSTRAINT UQ_nombre_caracteristica UNIQUE (nombre);

CREATE SEQUENCE SEQ_caracteristica_complementaria START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER SEQ_TRG_caracteristica_complementaria
BEFORE INSERT ON caracteristica_complementaria
REFERENCING NEW AS NEW FOR EACH ROW
BEGIN
  SELECT SEQ_caracteristica_complementaria.NEXTVAL INTO :NEW.id_caracteristica FROM DUAL;
END;
/

CREATE TABLE caracteristica_mascota (
  id_mascota        NUMBER(10)    NOT NULL,
  id_caracteristica NUMBER(10)    NOT NULL,
  valor             NVARCHAR2(25) NOT NULL,
  CONSTRAINT PK_caracteristica_mascota PRIMARY KEY (id_mascota, id_caracteristica)
);

CREATE TABLE mascota (
  id_mascota      NUMBER(10)               NOT NULL,
  nombre          VARCHAR2(15)             NOT NULL,
  foto            VARCHAR2(500)            NOT NULL,
  fec_nacimiento  DATE                     NOT NULL,
  sexo            CHAR                     NOT NULL,
  estatura        NUMBER(3,2)              NOT NULL,
  peso            NUMBER(5,2)              NOT NULL,
  id_tipo_mascota NUMBER(10)               NOT NULL,
  id_raza         NUMBER(10)               NOT NULL,
  fec_ingreso     TIMESTAMP WITH TIME ZONE NOT NULL,
  adoptado        NUMBER(1)                NOT NULL,
  discapacidad    NUMBER(1)                NOT NULL,
  CONSTRAINT PK_mascota PRIMARY KEY (id_mascota),
  CHECK (sexo IN ('F', 'M'))
);

ALTER TABLE mascota ADD CONSTRAINT UQ_nombre_mascota UNIQUE (nombre);
ALTER TABLE mascota ADD CONSTRAINT UQ_foto_mascota UNIQUE (foto);

CREATE SEQUENCE SEQ_mascota START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER SEQ_TRG_mascota
BEFORE INSERT ON mascota
REFERENCING NEW AS NEW FOR EACH ROW
BEGIN
  SELECT SEQ_mascota.NEXTVAL INTO :NEW.id_mascota FROM DUAL;
END;
/

COMMENT ON COLUMN mascota.foto IS 'url';
COMMENT ON COLUMN mascota.fec_nacimiento IS 'aproximada';
COMMENT ON COLUMN mascota.sexo IS 'F: femenino - M: masculino';
COMMENT ON COLUMN mascota.estatura IS 'metros';
COMMENT ON COLUMN mascota.peso IS 'kilos';
COMMENT ON COLUMN mascota.adoptado IS '0: no - 1: si';
COMMENT ON COLUMN mascota.discapacidad IS '0: no - 1: si';

CREATE TABLE raza (
  id_raza NUMBER(10)   NOT NULL,
  nombre  VARCHAR2(20) NOT NULL,
  CONSTRAINT PK_raza PRIMARY KEY (id_raza)
);

ALTER TABLE raza ADD CONSTRAINT UQ_nombre_raza UNIQUE (nombre);

CREATE SEQUENCE SEQ_raza START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER SEQ_TRG_raza
BEFORE INSERT ON raza
REFERENCING NEW AS NEW FOR EACH ROW
BEGIN
  SELECT SEQ_raza.NEXTVAL INTO :NEW.id_raza FROM DUAL;
END;
/

CREATE TABLE tipo_mascota (
  id_tipo_mascota NUMBER(10)   NOT NULL,
  nombre          VARCHAR2(20) NOT NULL,
  CONSTRAINT PK_tipo_mascota PRIMARY KEY (id_tipo_mascota)
);

ALTER TABLE tipo_mascota ADD CONSTRAINT UQ_nombre_tipo_mascota UNIQUE (nombre);

CREATE SEQUENCE SEQ_tipo_mascota START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER SEQ_TRG_tipo_mascota
BEFORE INSERT ON tipo_mascota
REFERENCING NEW AS NEW FOR EACH ROW
BEGIN
  SELECT SEQ_tipo_mascota.NEXTVAL INTO :NEW.id_tipo_mascota FROM DUAL;
END;
/

-- ============================
-- RELACIONES (FOREIGN KEYS)
-- ============================

ALTER TABLE mascota ADD CONSTRAINT FK_tipo_mascota_TO_mascota
  FOREIGN KEY (id_tipo_mascota)
  REFERENCES tipo_mascota (id_tipo_mascota);

ALTER TABLE mascota ADD CONSTRAINT FK_raza_TO_mascota
  FOREIGN KEY (id_raza)
  REFERENCES raza (id_raza);

ALTER TABLE caracteristica_mascota ADD CONSTRAINT FK_mascota_TO_caracteristica_mascota
  FOREIGN KEY (id_mascota)
  REFERENCES mascota (id_mascota);

ALTER TABLE caracteristica_mascota ADD CONSTRAINT FK_caracteristica_TO_caracteristica_mascota
  FOREIGN KEY (id_caracteristica)
  REFERENCES caracteristica_complementaria (id_caracteristica);
