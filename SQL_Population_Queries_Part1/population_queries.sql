-- The dataset covers year 2000 - 2010
SELECT DISTINCT year 
FROM population_years;

-- The largest population size for Gabon in this dataset is 1.54526 million.
SELECT year, MAX(population)
FROM population_years
WHERE country = "Gabon";

-- The 10 lowest population countries in 2005:
SELECT country, population
FROM population_years
WHERE year = 2005
ORDER BY 2 ASC
LIMIT 10;

-- All the distinct countries with a population of over 100 million in the year 2010 in ascending order:
SELECT DISTINCT country, population
FROM population_years
WHERE year = 2010 AND population > 100
ORDER BY 2 ASC;

-- Countries in this dataset have the word “Islands” in their name:
SELECT DISTINCT country
FROM population_years
WHERE country LIKE "%Islands%";

-- Difference in population between 2000 and 2010 in Indonesia:
-- In 2000: 214.67661 millions
SELECT country, population
FROM population_years
WHERE country = "Indonesia" AND year = 2000;

-- In 2010: 242.96834 millions
SELECT country, population
FROM population_years
WHERE country = "Indonesia" AND year = 2010;
-- Difference = 28.29173 millions