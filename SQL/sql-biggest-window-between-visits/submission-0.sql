-- Write your query below
with cte as (
select
user_id,
visit_date,
--LEAD(visit_date) over(partition by user_id order by visit_date) as next_date,
coalesce(LEAD(visit_date) over(partition by user_id order by visit_date),'2021-01-01') - visit_date as win
from user_visits
)
select
user_id,
max(win) as biggest_window
from cte
group by user_id
order by user_id