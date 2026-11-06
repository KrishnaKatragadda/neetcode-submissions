-- Write your query below
-- with cte as (
-- select team_id, count(*) as team_size
-- from employee
-- group by team_id
-- )
-- select e.employee_id,c.team_size
-- from employee e join cte c on 
-- e.team_id = c.team_id
select
e.employee_id, 
count(*) over(partition by e.team_id) as team_size
from employee e