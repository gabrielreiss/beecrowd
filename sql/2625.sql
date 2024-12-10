SELECT 
CAST(
SUBSTRING(np.cpf, 1, 3) +
'.'+
SUBSTRING(np.cpf, 4, 6) +
'.' +
SUBSTRING(np.cpf, 7, 9) +
'.' +
SUBSTRING(np.cpf, 10, 11)

AS character)
AS cpf
FROM natural_person AS np;


SELECT np.cpf MASKED WITH (FUNCTION = 'partial(3,"xxxxxx",3)')
FROM natural_person AS np;