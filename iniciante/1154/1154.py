#Faça um algoritmo para ler um número indeterminado de dados, 
# contendo cada um, a idade de um indivíduo. 
# O último dado, que não entrará nos cálculos, 
# contém o valor de idade negativa. Calcular e 
# imprimir a idade média deste grupo de indivíduos.

#Entrada
#A entrada contém um número indeterminado de inteiros. 
# A entrada será encerrada quando um valor negativo for lido.

#Saída
#A saída contém um valor correspondente à média de 
# idade dos indivíduos.

#A média deve ser impressa com dois dígitos após o 
# ponto decimal.

dados= []
cont = False

while cont == False:
    dados.append(int(input()))
    if dados[-1] < 0:
        cont = True

dados = dados[:-1] 

soma = 0

for i in range(0,len(dados)):
    soma += dados[i]

media = soma / len(dados)

print('{:.2f}'.format(media))