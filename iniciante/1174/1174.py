a = []

for i in range(0, 100):
    a.append(float(input()))

for i in range(0, 100):
    if a[i] <= 10:
        print('A[{}] = {}'.format(i, a[i]))