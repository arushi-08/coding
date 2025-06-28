-- Write your PostgreSQL query statement below


select p.product_id, coalesce(new_price, 10) as price
from (select distinct on(product_id) product_id, new_price
from products
where change_date <= to_date('2019-08-16', 'YYYY-mm-dd')
order by 1, change_date desc) as t
full outer join (select distinct product_id from products) as p
on t.product_id = p.product_id


