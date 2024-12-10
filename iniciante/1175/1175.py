n = []

for i in range(0, 20):
    n.append(int(input()))

aux = 0
for i in range(0,10):
    aux = n[i]
    n[i] = n[-(i+1)]
    n[-(i+1)] = aux

for i in range(0, 20):
    print('N[{}] = {}'.format(i, n[i]))