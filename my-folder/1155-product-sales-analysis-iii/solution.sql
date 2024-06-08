# Write your MySQL query statement below


-- select product id, year, quantity, and price for 1st year of every product sold

with t as (
    select product_id, min(year) as year
    from sales
    group by product_id
)
select product_id, year as first_year, quantity, price
from sales
where (year, product_id) in (select year, product_id from t)

