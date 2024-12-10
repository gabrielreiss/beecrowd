#Bob Conduite

n = int(input())

for i in range(0, n):
    dados = input().split()
    for j in range(0, len(dados)):
        dados[j] = int(dados[j])
    print(dados[0]+dados[1])