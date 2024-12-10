n = int(input())
media = []

for i in range(0,n):
    dados = input().split()
    for i in range(0,3):
        dados[i] = float(dados[i])
    media.append((dados[0]*2+dados[1]*3+dados[2]*5)/10)
for i in range(0,n):
    print('{:.1f}'.format(media[i]))
    