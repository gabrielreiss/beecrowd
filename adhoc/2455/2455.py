'''
p1 * c1 = p2 * c2

entrada: [p1, c1, p2, c2]

saída: 
    se equilibrada = 0
    se peso do 1 maior = -1
    se peso do 2 maior = 1
'''

p1, c1, p2, c2 = [int(i) for i in input().split(' ')]

if (p1 * c1) == (p2 * c2):
    print(0)
elif (p1 * c1) > (p2 * c2):
    print(-1)
else:
    print(1)

