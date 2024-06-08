# Write your MySQL query statement below

-- # unique subj each teacher teaches
select teacher_id, count(distinct(subject_id)) as cnt
from teacher
group by teacher_id
