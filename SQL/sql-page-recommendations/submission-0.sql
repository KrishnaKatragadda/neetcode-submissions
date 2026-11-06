-- Write your query below

with friends as (
select
case -- gives all the friends associated to user with id - 1
    when user1_id = 1 then user2_id
    else user1_id
end as friendship_id
from friendship
where user1_id = 1 or user2_id =1
)
select 
distinct 
l.page_id as recommended_page
from friends f join likes l -- i'm getting all the pages that friends have liked
on f.friendship_id = l.user_id
where NOT EXISTS ( -- if so, I will go ahead and not consider that
    select 1
    from likes m -- check if the page is already liked by user with id -1
    where m.user_id =1 and m.page_id = l.page_id
)