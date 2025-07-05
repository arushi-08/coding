-- Write your PostgreSQL query statement below


-- calculate 3 day rolling average
-- if not 3 days then its 3-day rolling avg not defined

select user_id, steps_date, rolling_average
from (select user_id, steps_date,
round(avg(steps_count) over(partition by user_id order by steps_date rows between 2 preceding and current row), 2) as rolling_average,
count(*) over(partition by user_id order by steps_date range between interval '2 days' preceding and current row) as pts_in_window
from steps)
where pts_in_window >= 3



