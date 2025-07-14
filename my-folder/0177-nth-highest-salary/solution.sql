CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN (
-- #Write your MySQL query statement below.
    
    SELECT DISTINCT salary
    FROM   (SELECT *,
        DENSE_RANK() OVER (ORDER BY salary desc) as rnk
    FROM employee) t
    WHERE rnk = n

);
END
