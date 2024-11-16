GRANT ALL PRIVILEGES ON who_wb_databases.* TO 'who_wb_user'@'localhost';

CREATE TABLE who_data (
    Country VARCHAR(50),
    Year INT,
    Underweight_adults FLOAT,
    Malaria_cases INT,
    NCD_deaths INT,
    PRIMARY KEY (Year)
);

CREATE TABLE worldbank_data (
    Country VARCHAR(50),
    Year INT,
    Labor_force FLOAT,
    Food_insecurity FLOAT,
    Agricultural_land FLOAT,
    Annual_growth FLOAT,
    PRIMARY KEY (Year)
);

SELECT * FROM who_data;

-- SQL query to identify countries with food insecurity > 50 and underweight adults < 20
SELECT wb.Country, wb.Year, wb.Food_insecurity, who.Underweight_adults, who.Malaria_cases
FROM worldbank_data wb
JOIN who_data who ON wb.Year = who.Year
WHERE wb.Food_insecurity > 10 AND who.Underweight_adults > 20;
