-- Write your PostgreSQL query statement below


-- find patient id, patient name, conditions of patients who have type 1 diabetes

SELECT *
FROM patients
WHERE conditions ~* '(^|[[:space:]])DIAB1'
