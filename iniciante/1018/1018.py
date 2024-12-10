n = int(input())
notas = [100,50,20,10,5,2,1]
r1 = []

#n = 576

for i in range(0,len(notas)):
    r1.append(n // notas[i])
    n = n % notas[i]
    
    print('{} nota(s) de R$ {:.2f}'.format(r1[i],notas[i]))



