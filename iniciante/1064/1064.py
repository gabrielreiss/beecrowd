dados= []
contador = 0
soma = 0
for i in range(0,6):
    dados.append(float(input()))
    if dados[i] > 0:
        contador += 1
        soma += dados[i]

media = soma / contador

print('{} valores positivos'.format(contador))
print('{:.1f}'.format(media))
