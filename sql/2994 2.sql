SELECT d.name, ROUND(SUM( att.hours * (1 + ws.bonus/100)),1) AS salary
FROM doctors AS d
INNER JOIN attendances AS att
ON att.id_doctor = d.id
INNER JOIN work_shifts AS ws
ON att.id_work_shift = ws.id
GROUP BY d.name;
