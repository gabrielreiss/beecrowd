n = int(input())
dados= []
c1 = 0
c2 = 0

for i in range(0,n):
    dados.append(int(input()))
    if 10 <= dados[i] <= 20:
        c1 += 1
    else:
        c2 +=1

print('{} in'.format(c1))
print('{} out'.format(c2))