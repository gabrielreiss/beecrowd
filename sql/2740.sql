SELECT 'Podium: ' || team
FROM league
WHERE 
position = 1 OR 
position = 2 OR
position = 3

UNION ALL

SELECT 'Demoted: ' || team
FROM league
WHERE
position = MAX(position)-1 OR
position = MAX(position);