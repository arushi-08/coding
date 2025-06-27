-- Write your PostgreSQL query statement below

-- find sales first year each product was sold


select s.product_id, year as first_year, quantity, price
from sales as s inner join (select product_id, min(year) as min_yr
                            from sales group by product_id) as t
on s.product_id = t.product_id and year = min_yr
