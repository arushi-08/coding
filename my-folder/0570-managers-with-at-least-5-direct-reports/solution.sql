# Write your MySQL query statement below

-- find managers with atleast 5 direct reports

select e.name as name
from employee as e inner join (
    select managerId
    from employee
    group by managerId
    having count(*) >= 5
) as me
on e.id = me.managerId
