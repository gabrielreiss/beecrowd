n = int(input())
dados = []

for i in range(0,n):
    soma = 0
    cont = 0
    dados.append(input().split())
    for j in range(0,2):
        dados[i][j] = int(dados[i][j])
    while cont < dados[i][1]:
        if dados[i][0] % 2 != 0:
            soma += dados[i][0]
            cont += 1
        dados[i][0] += 1
    print(soma)
    

