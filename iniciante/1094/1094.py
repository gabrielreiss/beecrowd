n = int(input())

soma = 0
coelho = 0
rato = 0
sapo = 0

for i in range(0,n):
    x = input().split()
    x[0] = int(x[0])
    soma += x[0]
    if x[1] == 'C':
        coelho += x[0]
    elif x[1] == 'R':
        rato += x[0]
    elif x[1] == 'S':
        sapo += x[0]

print('Total: {} cobaias'.format(soma))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))
print('Percentual de coelhos: {:.2f} %'.format(coelho/soma*100))
print('Percentual de ratos: {:.2f} %'.format(rato/soma*100))
print('Percentual de sapos: {:.2f} %'.format(sapo/soma*100))