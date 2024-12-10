#Faça um algoritmo para ler um valor A e um valor N. 
# Imprimir a soma de A para cada i com os valores (0 <= i <= N-1). 
# Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

#Entrada
#A entrada contém somente valores inteiros, 
# podendo ser positivos ou negativos. 
# Todos os valores estão na mesma linha.

#Saída
#A saída contém apenas um valor inteiro.

texto = input().split()

for i in range(0,len(texto)):
    texto[i] = int(texto[i])

a = texto[0]
n = 0

cont_n = 1

while n == 0:
    if texto[cont_n] > 0:
        n = texto[cont_n]
    cont_n += 1

soma = 0

for i in range(0,n):
    soma += a + i
print(soma)