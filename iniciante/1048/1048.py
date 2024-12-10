#A empresa ABC resolveu conceder um aumento de salários a seus funcionários 
# de acordo com a tabela abaixo:

#Salário	Percentual de Reajuste
#0 - 400.00             15%
#400.01 - 800.00        12%
#800.01 - 1200.00       10%
#1200.01 - 2000.00      7%
#Acima de 2000.00       4%

#Leia o salário do funcionário e calcule e mostre o novo salário, 
# bem como o valor de reajuste ganho e o índice reajustado, em percentual.

#Entrada
#A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

#Saída
#Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e 
# o percentual de reajuste ganho, conforme exemplo abaixo.

salario = float(input())

if 0 <= salario <= 400:
    reajuste = .15
elif 400 < salario <= 800:
    reajuste = 0.12
elif 800 < salario <= 1200:
    reajuste = 0.1
elif 1200 < salario <= 2000:
    reajuste = 0.07
elif salario > 2000:
    reajuste = 0.04

print('Novo salario: {:.2f}'.format(salario*(1+reajuste)))
print('Reajuste ganho: {:.2f}'.format(reajuste*salario))
print('Em percentual: {:.0f} %'.format(reajuste*100))