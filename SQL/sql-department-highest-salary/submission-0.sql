-- Write your query below
with deparment_salary as (
select e.name, e.salary, d.name as department_name, 
rank() over( partition by d.id order by e.salary desc) as rn
from employee e join department d on 
e.department_id = d.id
)
select department_name as department, name as employee, salary
from deparment_salary 
where rn = 1