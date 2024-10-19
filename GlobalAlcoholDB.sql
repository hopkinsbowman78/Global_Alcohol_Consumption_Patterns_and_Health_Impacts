-- Table: public.consumption_gdp

DROP TABLE IF EXISTS public.consumption_gdp;

CREATE TABLE IF NOT EXISTS public.consumption_gdp
(
    entity character varying(50) COLLATE pg_catalog."default" NOT NULL,
    code character varying(50) COLLATE pg_catalog."default",
    year text COLLATE pg_catalog."default" NOT NULL,
    total_alcohol_consumption_per_capita numeric(10,5),
    gdp_per_capita numeric(10,4),
    continent character varying(15) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.consumption_gdp
    OWNER to postgres;

select * from public.consumption_gdp

	

-- Table: public.fraction_of_mortality

DROP TABLE IF EXISTS public.fraction_of_mortality;

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

select * from public.fraction_of_mortality

-- Table: public.per_capita_litres

DROP TABLE IF EXISTS public.per_capita_litres;

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

select * from public.per_capita_litres

