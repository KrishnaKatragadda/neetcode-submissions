-- Write your query below
select e.employee_id
from employees e --level 1
JOIN employees m1 on e.manager_id = m1.employee_id -- level 2
JOIN employees m2 on m1.manager_id = m2.employee_id -- level 3
where m2.manager_id = 1 --making sure he is not CEO
and e.employee_id <>1 -- making sure he is not CEO