teste = int( input() )
for j in range(0, teste):

    n = int(input())
    soma = 0

    for i in range(1, n+1):
        if i % 2 != 0:
            soma += 1
        else:
            soma -= 1
    print(soma)