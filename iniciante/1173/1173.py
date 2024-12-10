x = int(input())

n = [x]

for i in range(1,10):
    n.append(2*n[i-1])

for i in range(0,10):
    print('N[{}] = {}'.format(i,n[i]))