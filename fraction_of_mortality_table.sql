-- Table: public.fraction_of_mortality

-- DROP TABLE IF EXISTS public.fraction_of_mortality;

CREATE TABLE IF NOT EXISTS public.fraction_of_mortality
(
    entity character varying(50) COLLATE pg_catalog."default" NOT NULL,
    code character varying(50) COLLATE pg_catalog."default" NOT NULL,
    year text COLLATE pg_catalog."default" NOT NULL,
    alcohol_attributable_fractions numeric(4,1) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.fraction_of_mortality
    OWNER to postgres;