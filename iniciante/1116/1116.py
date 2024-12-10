n = int(input())

for i in range(0,n):
    z = input().split()
    x = int(z[0])
    y = int(z[1])

    if y == 0:
        print('divisao impossivel')
    else:
        div = x / y
        print('{:.1f}'.format(div))