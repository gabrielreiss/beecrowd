dados = input().split()
for i in range(0,3):
    dados[i] = int(dados[i])

minimo = int()
medio = int()
maximo = int()

if dados[0] < dados[1] and dados[0] < dados[2]:
    minimo = dados[0]
    if dados[1] < dados[2]:
        medio = dados[1]
        maximo = dados[2]
    else:
        medio = dados[2]
        maximo = dados[1]
elif dados[1] < dados [0] and dados[1] < dados[2]:
    minimo = dados[1]
    if dados[0] < dados[2]:
        medio = dados[0]
        maximo = dados[2]
    else:
        medio = dados[2]
        maximo = dados[0]
elif dados[2] < dados[0] and dados[2] < dados[1]:
    minimo = dados[2]
    if dados[0] < dados[1]:
        medio = dados[0]
        maximo = dados[1]
    else:
        medio = dados[1]
        maximo = dados[0]

print(minimo)
print(medio)
print(maximo,'\n')

print(dados[0])
print(dados[1])
print(dados[2])