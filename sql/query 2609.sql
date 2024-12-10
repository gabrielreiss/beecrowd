SELECT c.name, SUM(p.amount) AS sum
FROM products p
INNER JOIN categories c
ON c.id = p.id_categories
GROUP BY c.name
ORDER BY c.name;

/* tira o order by para enviar*/