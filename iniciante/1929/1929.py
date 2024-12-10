dados = input().split()
tri = 'N'

aux = 0

for i in range(0, 4):
    dados[i] = int( dados[i] )

while dados[0] < dados[1] or dados[1] < dados[2] or dados[2] < dados[3]:
    for i in range(1, 4):
        if dados[i] > dados[i-1]:
            aux = dados[i]
            dados[i] = dados[i-1]
            dados[i-1] = aux

a = int(dados[0])
b = int(dados[1])
c = int(dados[2])
d = int(dados[3])

if (a <= b + c) or (a <= b + d) or (a <= c + d):
    tri = 'S'
elif (b <= a + c) or (b <= a + d) or (b <= c + d):
    tri = 'S'

print(tri)