# Write your MySQL query statement below


-- write a soln to calculate yoy growth rate for total spend for each product
-- 
-- 
-- 
-- 

with agg_spend_yr as (select extract(year from transaction_date) as year, product_id, sum(spend) as curr_year_spend
from user_transactions
group by product_id, extract(year from transaction_date)),

temp as (
    select a1.year, a1.product_id, a1.curr_year_spend, a2.curr_year_spend as prev_year_spend
from agg_spend_yr a1 left join agg_spend_yr a2
on a1.product_id = a2.product_id and a1.year - 1 = a2.year
)

select *,
(case when prev_year_spend then round((curr_year_spend - prev_year_spend) * 100 / prev_year_spend, 2) else null end) as yoy_rate
from temp
order by product_id, year

