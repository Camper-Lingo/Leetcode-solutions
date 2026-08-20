-- LeetCode #595
-- Big Countries
--
-- Find countries with an area of at least 3 million
-- or a population of at least 25 million.

SELECT NAME, POPULATION , AREA FROM WORLD
WHERE AREA >= 3000000 OR POPULATION >= 25000000