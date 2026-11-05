
select 
c.customer_id,
c.customer_name
from customers c join orders o 
on c.customer_id = o.customer_id 
-- now i have all the customers along with their orders
group by c.customer_id, c.customer_name
Having 
SUM( case when o.product_name ='A' then 1 else 0 end)>0
AND
SUM(case when o.product_name ='B' then 1 else 0 end)>0
AND
SUM(case when o.product_name ='C' then 1 else 0 end)=0 
-- checks if a customer has required assignment
order by customer_name