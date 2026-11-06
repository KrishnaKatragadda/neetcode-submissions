-- Write your query below
with cte as (
    select
    player_id,
    device_id,
    row_number() over(partition by player_id order by event_date) as rn
    from activity
)

select 
player_id,
device_id
from cte where rn=1