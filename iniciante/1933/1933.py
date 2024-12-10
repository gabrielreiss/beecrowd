#baralho 52 cartas
#13 cartas cada naipe

#baralho = []
#for j in range(0,4):
#    for i in range(1,14):
#        baralho.append(int(i))

dados = input().split()
a = int(dados[0])
b = int(dados[1])

carta = 13

if a == b:
    carta = a
elif a > b:
    carta = a
elif a < b:
    carta = b

print(carta)