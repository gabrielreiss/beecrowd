n = input().split('.')
n1 = int(n[0])
n2 = float(n[1])/100

notas = [100,50,20,10,5,2]
moedas = [ 1, 0.5, 0.25, 0.10, 0.05, 0.01]
r1 = []
r2 = []

for i in range(0, len(notas)):
    r1.append(n1 // notas[i])
    n1 = n1 % notas[i]
    
    print('{} nota(s) de R$ {:.2f}'.format(r1[i],notas[i]))

n2 += n1

for i in range(0, len(moedas)):
    r2.append(n2 // moedas[i])
    n2 = n2 %  moedas[i]
    print('{:.0f} moeda(s) de R$ {:.2f}'.format(r2[i],moedas[i]))


