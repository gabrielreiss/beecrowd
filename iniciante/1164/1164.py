n = int(input())

for j in range(0,n):
    x = int(input())
    lista=[]
    for i in range(1,x):
        if x % i == 0:
            lista.append(i)
    
    soma = sum(lista)  

    if soma == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
