notas_validas = 0
notas = 0
soma = 0

while notas_validas < 2:
    #if notas_validas == 2:
    #else:
    notas = float(input())
    if 0 <= notas <= 10:
        soma += notas
        notas_validas += 1
    else:
        print('nota invalida')

media = soma / notas_validas
print('media = {:.2f}'.format(media))