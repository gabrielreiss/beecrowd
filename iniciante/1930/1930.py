dados = input().split()

for i in range(0, len(dados)):
    dados[i] = int(dados[i])

soma = 0

for i in range(0, len(dados)-1):
    soma += dados[i] - 1

soma += dados[len(dados)-1]

print(soma)