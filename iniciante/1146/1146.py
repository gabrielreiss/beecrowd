cont = False

while cont == False:
    x = int(input())

    if x != 0:
        texto=''
        for i in range(1,x+1):
            texto += str(i) + ' '
        print(texto[:-1])
    else:
        cont = True
