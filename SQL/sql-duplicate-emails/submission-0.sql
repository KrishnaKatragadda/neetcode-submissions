-- Write your query below

select 
email
from person 
group by email
having count(*)>1