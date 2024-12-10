SELECT p.name, c.name
FROM products AS p
JOIN categories AS c
ON p.id_categories = c.id
WHERE amount > 100 AND
( c.id = 1 OR 
  c.id = 2 OR 
  c.id = 3 OR
  c.id = 6 OR
  c.id = 9
)
ORDER BY c.id;