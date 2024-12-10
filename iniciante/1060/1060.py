dados= []
contador = 0
for i in range(0,6):
    dados.append(float(input()))
    if dados[i] > 0:
        contador += 1

print('{} valores positivos'.format(contador))