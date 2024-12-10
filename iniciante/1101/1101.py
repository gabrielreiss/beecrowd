n = []
m = []
soma = []
controle = False

while controle == False:
    par=input().split()
    n.append(int(par[0]))
    m.append(int(par[1]))
    if n[len(n)-1] == 0 or m[len(m)-1] == 0:
        controle = True

for j in range(0,len(n)-1):
    soma.append(0)
    if n[j] <=m[j]:
        for i in range(n[j],m[j]+1):
            soma[j] += i
        #print('{} {} {} {} Sum={}'.format(n[j],n[j]+1,m[j]-1,m[j],soma[j]))
    else:
        for i in range(m[j],n[j]+1):
            soma[j] += i
    print('{} {} {} {} Sum={}'.format(m[j],m[j]+1,n[j]-1,n[j],soma[j]))


#5 2
#6 3
#5 0

#2 3 4 5 Sum=14
#3 4 5 6 Sum=18