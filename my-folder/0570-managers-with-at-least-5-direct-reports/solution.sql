# Write your MySQL query statement below

select name from
employee 
where id in (
    select managerId
    from (
        select *, ifnull(managerId, 0)
        from employee
    ) as e
    group by managerId
    having count(id) >= 5
)
