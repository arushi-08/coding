# Write your MySQL query statement below


select *
from users
where regexp_like(mail, '^[A-Za-z][A-Za-z_0-9\.\-]*@leetcode(\\?com)?\\.com$')

