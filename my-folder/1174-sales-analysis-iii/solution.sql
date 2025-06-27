-- Write your PostgreSQL query statement below

-- only sold in first quarter


with qtr_sales as (select product_id
from sales
group by product_id
having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31')

select product_id, product_name
from product
where product_id in (select * from qtr_sales)
