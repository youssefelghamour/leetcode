/*
  This query calculates the number of times each student attended each exam

  1. CROSS JOIN:
     - Combines every student with every subject
     - Ensures we have all possible combinations of students and subjects, even if a student didn’t attend a subject’s exam
     - Like a left join on both of them, gets all students and all subjects

  2. LEFT JOIN:
     - Joins the result of the CROSS JOIN with the Examinations table
     - Ensures we include all student-subject pairs, even if a student didn't attend the exam (attendance count will be 0)

  3. COUNT:
     - Counts how many times each student attended each subject's exam by counting matching rows in the Examinations table

  4. GROUP BY:
     - Groups the result by student_id and subject_name to get the attendance count for each student-subject pair

  5. ORDER BY:
     - Orders the result by student_id and subject_name to ensure the output is sorted as requested
*/
SELECT 
    s.student_id, 
    s.student_name, 
    sub.subject_name, 
    COUNT(e.subject_name) AS attended_exams
FROM 
    Students s
CROSS JOIN 
    Subjects sub
LEFT JOIN
    Examinations e
    ON s.student_id = e.student_id
    AND sub.subject_name = e.subject_name
GROUP BY
    s.student_id,
    sub.subject_name
ORDER BY
    s.student_id,
    sub.subject_name;