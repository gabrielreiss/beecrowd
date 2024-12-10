nv = True

n = 0
gols = []
inter = 0
gremio = 0
empate = 0

while nv == True:

    gols = input().split()
    n += 1

    gols[0] = int(gols[0])
    gols[1] = int(gols[1])
    #gols[0] é inter
    #gols[1] é gremio

    if gols[0] > gols[1]:
        inter += 1
    elif gols[0] < gols[1]:
        gremio += 1
    elif gols[0] == gols[1]:
        empate += 1

    print('Novo grenal (1-sim 2-nao)')
    repetir = input()
    if repetir != '1':
        nv = False

print('{} grenais'.format(n))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))

if inter > gremio:
    print('Inter venceu mais')
elif inter < gremio:
    print('Gremio venceu mais')
elif inter == gremio:
    print('Nao houve vencedor')