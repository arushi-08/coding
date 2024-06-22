# Write your MySQL query statement below

with t as (
    select seller_id, sum(price) as p
    from sales
    group by seller_id
    )

select seller_id
from t
where p = (select max(p) from t)
