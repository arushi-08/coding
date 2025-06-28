-- Write your PostgreSQL query statement below

-- author = viewer

select distinct v.author_id as id
from views v inner join views v2
on v.author_id = v2.viewer_id and v.article_id = v2.article_id

-- select *
-- from views 
-- where viewer_id = 1

-- select *
-- from views v inner join views v2
-- on v.author_id = v2.viewer_id
-- where v.author_id = 1
