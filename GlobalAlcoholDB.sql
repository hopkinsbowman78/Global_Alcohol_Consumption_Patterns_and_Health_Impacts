-- Drop and Create Table: public.alcohol_consumption_vs_gdp
DROP TABLE IF EXISTS public.alcohol_consumption_vs_gdp;

CREATE TABLE public.alcohol_consumption_vs_gdp (
    entity VARCHAR(50) NOT NULL,
    year TEXT NOT NULL,
    alcohol_consumption_per_capita NUMERIC(7,5) NOT NULL,
    alcohol_consumption_vs_gdp NUMERIC(10,4) NOT NULL,
    PRIMARY KEY (entity, year)
);

ALTER TABLE public.alcohol_consumption_vs_gdp
    OWNER TO postgres;

-- View data in alcohol_consumption_vs_gdp
SELECT * FROM public.alcohol_consumption_vs_gdp;



-- Drop and Create Table: public.alcohol_related_mortality
DROP TABLE IF EXISTS public.alcohol_related_mortality;

CREATE TABLE public.alcohol_related_mortality (
    entity VARCHAR(50) NOT NULL,
    year TEXT NOT NULL,
    alcohol_related_mortality NUMERIC(4,1) NOT NULL,
    PRIMARY KEY (entity, year)
);

ALTER TABLE public.alcohol_related_mortality
    OWNER TO postgres;

-- View data in alcohol_related_mortality
SELECT * FROM public.alcohol_related_mortality;
