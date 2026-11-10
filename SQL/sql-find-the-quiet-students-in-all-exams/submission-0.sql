-- Write your query below
with min_max as (
select
exam_id,
student_id,
score,
rank() over(partition by exam_id order by score desc) as max_score_student,
rank() over(partition by exam_id order by score) as min_score_student
from exam
), student_max_min as (
    select student_id
    from min_max
    where max_score_student = 1 OR min_score_student = 1
)
select s.student_id,s.student_name
from student s LEFT JOIN student_max_min sm
on s.student_id = sm.student_id
where sm.student_id is NULL 
and EXISTS (
    select 1 -- checking if there is a matching records of student in exam table
    from exam e 
    where e.student_id = s.student_id
)
order by student_id 