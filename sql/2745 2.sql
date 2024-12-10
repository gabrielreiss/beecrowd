SELECT name, CAST(salary* 0.1 AS decimal(10,2))
FROM people
WHERE salary > 3000;