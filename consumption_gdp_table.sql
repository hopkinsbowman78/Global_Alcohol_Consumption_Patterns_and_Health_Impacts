-- Table: public.consumption_gdp

-- DROP TABLE IF EXISTS public.consumption_gdp;

CREATE TABLE IF NOT EXISTS public.consumption_gdp
(
    entity character varying(50) COLLATE pg_catalog."default" NOT NULL,
    code character varying(50) COLLATE pg_catalog."default" NOT NULL,
    year text COLLATE pg_catalog."default" NOT NULL,
    total_alcohol_consumption_per_capita numeric(10,5),
    gdp_per_capita numeric(10,4),
    continent character varying(15) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.consumption_gdp
    OWNER to postgres;