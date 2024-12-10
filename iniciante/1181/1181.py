n_linha = int(input())
operacao = input()

m =[]
linha = []
for i in range(0,12):
    for j in range(0,12):
        linha.append(float(input()))
    m.append(linha)
    linha =[]

#import numpy as np
#matriz = np.matrix(m)
if operacao == 'S':
    print(sum(m[n_linha]))
elif operacao == 'M':
    print(
        sum(m[n_linha])/len(m[n_linha])
        )