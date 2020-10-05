-- 56 entries in the database are from Africa:
SELECT count(*)
FROM countries
WHERE continent = "Africa";

-- The total population of Oceania in 2005 is 32.66417 millions:
SELECT SUM(p.population)
FROM countries AS c
JOIN population_years AS p
ON c.id = p.country_id
WHERE c.continent = "Oceania" AND p.year = 2005;

-- The average population of countries in South America in 2003 is 25.89 millions:
SELECT AVG(p.population)
FROM countries AS c
JOIN population_years AS p
ON c.id = p.country_id
WHERE c.continent = "South America" AND p.year = 2003;

-- Niue had the smallest population in 2007 (0.00216 million):
SELECT c.name, MIN(p.population)
FROM countries AS c
JOIN population_years AS p
ON c.id = p.country_id
WHERE p.year = 2007;

-- The average population of Poland during the time period covered by this dataset is 38.56 millions:
SELECT AVG(p.population)
FROM countries AS c
JOIN population_years AS p
ON c.id = p.country_id
WHERE c.name = "Poland";

-- 4 countries have the word "The" in their name:
SELECT COUNT(id)
FROM countries
WHERE name LIKE "%The%";

-- The total population of each continent in 2010:
SELECT c.continent, SUM(p.population)
FROM countries AS c
JOIN population_years AS p
ON c.id = p.country_id
WHERE p.year = 2010
GROUP BY c.continent;

