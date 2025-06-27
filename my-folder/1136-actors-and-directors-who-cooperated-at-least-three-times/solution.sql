-- Write your PostgreSQL query statement below


-- find all pairs (actor_id, director_id)

select actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) > 2
