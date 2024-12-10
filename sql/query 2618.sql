/* 
O setor de importação da nossa empresa precisa de um relatório 
sobre a importação de produtos do nosso fornecedor Sansul.

Sua tarefa é exibir o nome dos produtos, o nome do fornecedor e o nome da categoria, 
para os produtos fornecidos pelo fornecedor ‘Sansul SA’ e cujo nome da categoria seja 'Imported'.
*/

SELECT pd.name, pv.name, c.name
FROM products pd
INNER JOIN providers pv
ON pd.id_providers = pv.id
INNER JOIN categories c
ON c.id = pd.id_categories  
WHERE pv.name = 'Sansul SA'
AND c.name = 'Imported';


SELECT *
FROM products pd
INNER JOIN providers pv
ON pd.id_providers = pv.id;
INNER JOIN categories c
ON c.id = pd.id_categories;