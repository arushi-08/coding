# Write your MySQL query statement below



select Department, Employee, Salary
from (
        select d.name as Department, e.name as Employee, salary as Salary, dense_rank() over
        (partition by d.name order by salary desc) as drnk
    from employee e left join department d
    on e.departmentId = d.id
) as j
where drnk <= 3
