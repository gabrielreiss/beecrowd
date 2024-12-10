dados = []
pares = 0
impar = 0
positivo = 0
negativo = 0

for i in range(0,5):
    dados.append(int(input()))
    if dados[i] % 2 == 0:
        pares += 1
    else:
        impar += 1
    
    if dados[i] > 0:
        positivo += 1
    elif dados[i] < 0:
        negativo += 1

print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))