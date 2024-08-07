# Write your MySQL query statement below


with reporting_table as (
select reports_to as manager_id, count(employee_id) as reports_count, round(avg(age)) as average_age
from employees
group by reports_to
)

select e.employee_id, e.name, rt.reports_count, rt.average_age
from employees e join reporting_table rt
on e.employee_id = rt.manager_id
order by e.employee_id


-- 50 + 35 + 48
