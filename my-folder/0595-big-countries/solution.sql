-- Write your PostgreSQL query statement below

-- country is big if

select name, population, area
from world
where population >= 25000000 or area >= 3000000
