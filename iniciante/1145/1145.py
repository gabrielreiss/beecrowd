n = input().split()
x = int(n[0])
y = int(n[1])

linhas = y // x
cont = 0

texto = ''

#while cont < y:

for i in range(0,linhas):
    for j in range(0,x):
        texto += str(i*x+j+1) + ' '
    print(texto[0:(x*x-1)])
    texto=''