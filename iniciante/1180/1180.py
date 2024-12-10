n = int(input())
dados = input().split()

x = []

for i in range(0, n):
    x.append(int(dados[i]))

menor = x[0]
posicao = 0

for i in range(1, n):
    if x[i] < x[i-1]:
        menor = x[i]
        posicao = i

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(posicao))