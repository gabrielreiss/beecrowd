n = int(input())

for i in range(0,n):
    x = int(input())
    dados = []

    for i in range(1,x+1):
        if x % i == 0:
            dados.append(i)

    if len(dados)==2:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))