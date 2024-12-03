
CREATE TABLE auto (
                rekisterinumero VARCHAR(7) NOT NULL,
                malli VARCHAR(30) NOT NULL,
                merkki VARCHAR(30) NOT NULL,
                vuosimalli CHAR(4) NOT NULL,
                CONSTRAINT auto_pk PRIMARY KEY (rekisterinumero)
);
COMMENT ON TABLE auto IS 'Ajoneuvon perustiedot';


CREATE TABLE ryhma (
                ryhma VARCHAR(35) NOT NULL,
                vastuuhenkilo VARCHAR(50),
                CONSTRAINT ryhma_pk PRIMARY KEY (ryhma)
);
COMMENT ON TABLE ryhma IS 'Opiskelijan luokka';
COMMENT ON COLUMN ryhma.ryhma IS 'Ryhm�n nimi, esim. auto22B tai henkil�kunta';
COMMENT ON COLUMN ryhma.vastuuhenkilo IS 'Vastuuopettaja tai lehiesimies';


CREATE TABLE lainaaja (
                hetu CHAR(11) NOT NULL,
                etunimi VARCHAR(35) NOT NULL,
                sukunimi VARCHAR(35) NOT NULL,
                ryhma VARCHAR(35) NOT NULL,
                ajokorttiluokka VARCHAR(10) NOT NULL,
                sahkoposti VARCHAR(35),
                CONSTRAINT lainaaja_pk PRIMARY KEY (hetu)
);
COMMENT ON TABLE lainaaja IS 'Lainaajan (opiskelija tai opettaja) perustiedot';
COMMENT ON COLUMN lainaaja.hetu IS 'Kansallinen henkil�tunnus';
COMMENT ON COLUMN lainaaja.ryhma IS 'Ryhm�n nimi, esim. auto22B tai henkil�kunta';
COMMENT ON COLUMN lainaaja.ajokorttiluokka IS 'Esim AB tai ABCE';
COMMENT ON COLUMN lainaaja.sahkoposti IS 'Rasekon s�hk�postiosoite';


CREATE SEQUENCE lainaus_lainausnumero_seq;

CREATE TABLE lainaus (
                lainausnumero INTEGER NOT NULL DEFAULT nextval('lainaus_lainausnumero_seq'),
                hetu CHAR(11) NOT NULL,
                rekisterinumero VARCHAR(7) NOT NULL,
                lainausaika TIMESTAMP NOT NULL,
                palautus TIMESTAMP,
                CONSTRAINT lainaus_pk PRIMARY KEY (lainausnumero)
);
COMMENT ON TABLE lainaus IS 'Lainaustapahtuman tiedot';
COMMENT ON COLUMN lainaus.lainausnumero IS 'Lainaustapahtumalle automaattisesti annettava juokseva numero';
COMMENT ON COLUMN lainaus.hetu IS 'Kansallinen henkil�tunnus';
COMMENT ON COLUMN lainaus.lainausaika IS 'P�iv�m��r� ja kellonaika, kun auto on otettu lainaan.';
COMMENT ON COLUMN lainaus.palautus IS 'Palautuksen p�iv� ja kellonaika';


ALTER SEQUENCE lainaus_lainausnumero_seq OWNED BY lainaus.lainausnumero;

ALTER TABLE lainaus ADD CONSTRAINT auto_lainaus_fk
FOREIGN KEY (rekisterinumero)
REFERENCES auto (rekisterinumero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE lainaaja ADD CONSTRAINT ryhma_lainaaja_fk
FOREIGN KEY (ryhma)
REFERENCES ryhma (ryhma)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE lainaus ADD CONSTRAINT lainaaja_lainaus_fk
FOREIGN KEY (hetu)
REFERENCES lainaaja (hetu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
