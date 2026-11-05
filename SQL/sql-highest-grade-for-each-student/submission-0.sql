with ranked_customers AS (
select
student_id,
exam_id,
score,
ROW_NUMBER() OVER(partition by student_id 
order by score desc, exam_id asc) rn
from exam_results
)
select 
student_id,
exam_id,
score
from ranked_customers 
where rn = 1
order by student_id 