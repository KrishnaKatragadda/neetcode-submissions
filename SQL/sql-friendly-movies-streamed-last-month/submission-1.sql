-- Write your query below
select
distinct c.title
from tv_program p join content c 
on p.content_id = c.content_id
where c.kids_content ='Y' and c.content_type ='Movies'
and p.program_date >='2020-06-01'  and p.program_date < '2020-07-01'