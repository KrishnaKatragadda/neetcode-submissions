-- Write your query below
with cte as (
select
o.order_id, o.order_date,c.customer_id,c.name as customer_name,
row_number() over(partition by o.customer_id order by o.order_date desc) as rn
from customers c join orders o 
on o.customer_id = c.customer_id
)
select customer_name, customer_id,order_id, order_date
from cte
where rn<=3
order by customer_name asc, customer_id asc, order_date desc