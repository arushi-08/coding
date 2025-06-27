-- Write your PostgreSQL query statement below


-- write a soln to calculate total time in mins spent by each emp on each day 
-- time spent, sum group by


select event_day as day, emp_id, sum(out_time - in_time) as total_time
from employees
group by emp_id, event_day


