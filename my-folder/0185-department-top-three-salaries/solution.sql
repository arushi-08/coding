

-- top 3 uniq 
With join_data_idx As
(SELECT
    d.name as department,
    e.name as employee,
    salary,
    DENSE_RANK() OVER(PARTITION BY d.id ORDER BY salary DESC) as rn
FROM employee e
JOIN department d
    ON e.departmentid = d.id)


SELECT
    department, employee, salary
FROM join_data_idx
WHERE rn <= 3
