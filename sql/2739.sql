SELECT name, CAST(EXTRACT(DAY FROM payday) as INT)
FROM loan;