#area inferior da diagonal principal

operacao = input()

m =[]
linha = []
for i in range(0,12):
    for j in range(0,12):
        linha.append(float(input()))
    m.append(linha)
    linha =[]

soma = 0
cont = 0

for i in range(0,12):
    for j in range(0,12):
        if (11-j) > i:
            soma += m[i][j]
            cont += 1


if operacao == 'S':
    print('{:.1f}'.format(soma))
elif operacao == 'M':
    print('{:.1f}'.format(soma/cont))