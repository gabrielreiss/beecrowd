controle = False
n=[]

while controle == False:
    n.append(input().split())
    n[len(n)-1][0] = int(n[len(n)-1][0])
    n[len(n)-1][1] = int(n[len(n)-1][1])
    if n[len(n)-1][0] == n[len(n)-1][1]:
        controle = True

texto = []

for i in range(0,len(n)-1):
    if n[i][0] < n[i][1]:
        texto.append("Crescente")
    else:
        texto.append("Decrescente")

for i in range(0,len(texto)):
    print(texto[i])