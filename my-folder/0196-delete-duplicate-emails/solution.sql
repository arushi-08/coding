# Write your MySQL query statement below

with t as (select *, row_number() over(partition by email order by id) as rn
from person
)

delete from person
where id in (select id from t where t.rn > 1)  
