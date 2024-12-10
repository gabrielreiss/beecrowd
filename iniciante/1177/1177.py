t = int(input())
cont = 0
n = []

while cont < 1000:
    for i in range(0,t):
        n.append(i)
        cont += 1

for i in range(0,1000):
    print('N[{}] = {}'.format(i, n[i]))
    