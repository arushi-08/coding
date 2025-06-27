# Write your MySQL query statement below


select product_id,
coalesce(
    (select new_price 
    from products as ph
    where ph.product_id = p.product_id
    and ph.change_date <= '2019-08-16'
    order by ph.change_date desc
    limit 1),
    10
) as price
from
(
    select distinct product_id
    from products
) as p
