n_coluna= int(input())
operacao = input()

m =[]
linha = []
for i in range(0,12):
    for j in range(0,12):
        linha.append(float(input()))
    m.append(linha)
    linha =[]

soma = 0
for i in range(0,12):
    soma += m[i][n_coluna]

if operacao == 'S':
    print('{:.2f}'.format(soma))
elif operacao == 'M':
    print('{:.2f}'.format(soma/12))

#import numpy as np
#matriz = np.matrix(m)

#if operacao == 'S':
#    print('{:2.f}'.format(sum(matriz[:,n_coluna])))
#elif operacao == 'M':
#    print('{:2.f}'.format(sum(matriz[:,n_coluna])/len(matriz[:,n_coluna])))

        