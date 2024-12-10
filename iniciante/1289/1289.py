x = int(input())

def prob(dados):
    # 2 0.166666 1

    n = int(dados[0])
    p = float(dados[1])
    i = int(dados[2])

    q = 1 - p
    w = p * ( q ** ( i - 1 ) ) / ( 1- ( q ** n ) )
    return w

#a = []
#for i in range(0, x):
#    dados = input().split()
#    a.append(prob(dados))

#for i in range(0, x):
#    print('{:.4f}'.format(a[i]))

for i in range(0, x):
    dados = input().split()
    print('{:.4f}'.format(prob(dados)))