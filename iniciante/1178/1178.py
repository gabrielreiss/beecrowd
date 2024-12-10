x = float(input())

n = []
n.append(x)

for i in range(1,100):
    n.append(n[i-1]/2)

for i in range(0,100):
    print('N[{}] = {:.4f}'.format(i, n[i]))