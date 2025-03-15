SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET default_tablespace = '';
SET default_with_oids = false;

---
--- drop tables
---

DROP TABLE IF EXISTS Alunos;

--
-- Name: Alunos; Type: TABLE
--

CREATE TABLE Alunos (
    aluno_id smallint PRIMARY KEY NOT NULL,
    aluno_name character varying(70) NOT NULL,
    aluno_ra character varying(6) NOT NULL
);

--
-- Data for Name: Alunos
--

INSERT INTO Alunos VALUES (1, 'Fabio', '123456');
INSERT INTO Alunos VALUES (2, 'Thayna', '456789');
INSERT INTO Alunos VALUES (3, 'Emerson', '235689');
INSERT INTO Alunos VALUES (4, 'Alison', '231435');
INSERT INTO Alunos VALUES (5, 'Marcelo', '987654');
INSERT INTO Alunos VALUES (6, 'Carol', '238890');

