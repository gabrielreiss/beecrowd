qt = int( input() )

#a soma desses números for par o jogador 
#que escolheu PAR ganha ou vice verso

for q in range(0, qt):
    dados = input().split()
    n = input().split()
    n[0] = int( n[0] )
    n[1] = int( n[1] )

    soma = n[0] + n[1]
    r = ''
    if soma % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'

    if dados[1] == r:
        print(dados[0])
    else:
        print(dados[2])