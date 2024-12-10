n = int(input())
dados = input().split()

for i in range(0, n):
    dados[i] = int(dados[i])

pessoa = 0
menor = dados[i]

for i in range(1, n):
    if dados[i] < menor:
        pessoa = i
        menor = dados[i]

print(pessoa + 1) 