select name
from customers 
where id not in (select distinct customer_id from orders)