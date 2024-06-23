# Write your MySQL query statement below

with st as (select * from students cross join subjects),
e as (select student_id, subject_name, count(*) as attended_exams from examinations group by student_id, subject_name)

select st.student_id, student_name, st.subject_name, ifnull(attended_exams, 0) as attended_exams
from st left join e
on st.student_id=e.student_id and st.subject_name = e.subject_name
group by st.student_id, st.subject_name
order by st.student_id, st.subject_name
