m2 = 0
m3 = 0
m4 = 0
m5 = 0

n = int(input())
dados = input().split()

for i in range(0, n):
    dados[i] = int(dados[i])
    if dados[i] % 2 == 0:
        m2 += 1
    if dados[i] % 3 == 0:
        m2 += 1
    if dados[i] % 4 == 0:
        m4 += 1
    if dados[i] % 5 == 0:
        m5 += 1

print('{} Multiplo(s) de 2'.format(m2))
print('{} Multiplo(s) de 3'.format(m3))
print('{} Multiplo(s) de 4'.format(m4))
print('{} Multiplo(s) de 5'.format(m5))