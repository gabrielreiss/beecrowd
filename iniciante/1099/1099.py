n = int(input())

x = []
soma = []

for i in range(0,n):
    x.append(input().split())
    x[i][0] = int(x[i][0])
    x[i][1] = int(x[i][1])
    soma.append(int(0))

    if x[i][0] < x[i][1]:
        inicial = x[i][0]
        final = x[i][1]
    else:
        inicial = x[i][1]
        final = x[i][0]
    for j in range(inicial+1,final):
        if j % 2 != 0:
            soma[i] += j

for i in range(0,n):
    print(soma[i])
