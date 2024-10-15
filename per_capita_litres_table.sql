-- Table: public.per_capita_litres

-- DROP TABLE IF EXISTS public.per_capita_litres;

CREATE TABLE IF NOT EXISTS public.per_capita_litres
(
    entity character varying(50) COLLATE pg_catalog."default" NOT NULL,
    code character varying(50) COLLATE pg_catalog."default",
    year text COLLATE pg_catalog."default" NOT NULL,
    total_alcohol_consumption_per_capita numeric(7,5) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.per_capita_litres
    OWNER to postgres;