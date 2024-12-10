dado=[]
for i in range(0,10):
    dado.append(int(input()))
    if dado[-1] <= 0:
        dado[-1] = 1

for i in range(0, 10):
    print('X[{}] = {}'.format(i,dado[i]))
