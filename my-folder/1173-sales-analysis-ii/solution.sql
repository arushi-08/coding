# Write your MySQL query statement below

with t as (select s.buyer_id, p.product_name from sales as s left join product as p
on s.product_id = p.product_id
group by s.buyer_id, p.product_name)

select buyer_id
from t
where buyer_id not in (select buyer_id from t where product_name = 'iPhone')
and product_name = 'S8'

-- select buyer_id
-- from sales as s left join product as p
-- on s.product_id = p.product_id
-- group by s.buyer_id, p.product_name
-- having p.product_name = 'S8' and p.product_name != 'iPhone'
