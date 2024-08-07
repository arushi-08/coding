# Write your MySQL query statement below


select s1.id, ifnull((
    case when s1.id % 2 = 1 then s2.student
    else s3.student end
    ), s1.student) as student
from seat s1 left join seat s2 
on s1.id + 1 = s2.id 
left join seat s3
on s1.id = s3.id + 1

