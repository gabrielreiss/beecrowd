/*
Na hora de entregar o relatório de quantos produtos a empresa tem em estoque, 
uma parte do relatório ficou corrompida, por isso o responsável do estoque lhe pediu uma ajuda, 
ele quer que você exiba os seguintes dados para ele.

Exiba o nome dos produtos cujas quantidades estejam entre 10 e 20 e cujo nome do fornecedor inicie com a letra ‘P’.
*/

SELECT pd.name
FROM products pd
INNER JOIN providers pv
ON pv.id = pd.id_providers
WHERE pd.amount BETWEEN 10 and 20
AND pv.name LIKE 'P%';