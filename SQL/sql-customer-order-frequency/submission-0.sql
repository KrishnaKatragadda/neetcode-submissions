-- Write your query below
select
c.customer_id, c.name
from orders o join product p 
on o.product_id = p.product_id
join customers c on c.customer_id = o.customer_id
where o.order_date >='2020-06-01' and o.order_date <='2020-07-31'
group by c.customer_id,c.name
having 
(
    sum(case when o.order_date >='2020-06-01' and o.order_date <='2020-06-30' then o.quantity*p.price end)>=100
AND 
sum(case when o.order_date >='2020-07-01' and o.order_date <='2020-07-31' then o.quantity*p.price
end)>=100
)