cont = 0

par = []
impar = []

cont_par = 0
cont_impar = 0

while cont < 15:
    x = int(input())
    
    if x % 2 == 0:
        par.append(x)
        if len(par) == 5:
            for i in range(0,5):
                print('par[{}] = {}'.format(i, par[i]))
            par = []
    else:
        impar.append(x)
        if len(impar) == 5:
            for i in range(0,5):
                print('impar[{}] = {}'.format(i, impar[i]))
            impar = []
    cont += 1

for i in range(0,len(impar)):
    print('impar[{}] = {}'.format(i, impar[i]))

for i in range(0, len(par)):
    print('par[{}] = {}'.format(i, par[i]))
