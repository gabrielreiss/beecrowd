SELECT l.name, 
CAST(l.omega*1.618 as decimal(10,3))
FROM life_registry as l
LEFT JOIN dimensions as d
ON d.id = l.dimensions_id
WHERE l.name LIKE 'Richard%' AND
d.name in ('C875', 'C774')
ORDER BY l.omega;