--  Create the Global Alcohol Database
-- CREATE DATABASE GlobalAlcoholDB;

-- Connect to the new database
-- \c GlobalAlcoholDB



-- Create the Table: public.alcohol_consumption_per_capita

DROP TABLE IF EXISTS public.alcohol_consumption_per_capita;

CREATE TABLE IF NOT EXISTS public.alcohol_consumption_per_capita
(
    entity character varying(50) COLLATE pg_catalog."default" NOT NULL,
    year text COLLATE pg_catalog."default" NOT NULL,
    alcohol_consumption_per_capita numeric(7,5) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.alcohol_consumption_per_capita
    OWNER to postgres;

select * from public.alcohol_consumption_per_capita



-- Create the Table: public.alcohol_consumption_vs_gdp

DROP TABLE IF EXISTS public.alcohol_consumption_vs_gdp;

CREATE TABLE IF NOT EXISTS public.alcohol_consumption_vs_gdp
(
    entity character varying(50) COLLATE pg_catalog."default" NOT NULL,
    year text COLLATE pg_catalog."default" NOT NULL,
    alcohol_consumption_per_capita numeric(7,5) NOT NULL,
    alcohol_consumption_vs_gdp numeric(10,4) COLLATE pg_catalog."default" NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.alcohol_consumption_vs_gdp
    OWNER to postgres;

select * from public.alcohol_consumption_vs_gdp

	

-- Create the Table: public.alcohol_related_mortality

DROP TABLE IF EXISTS public.alcohol_related_mortality;

CREATE TABLE IF NOT EXISTS public.alcohol_related_mortality
(
    entity character varying(50) COLLATE pg_catalog."default" NOT NULL,
    year text COLLATE pg_catalog."default" NOT NULL,
    alcohol_related_mortality numeric(4,1) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.alcohol_related_mortality
    OWNER to postgres;

select * from public.alcohol_related_mortality