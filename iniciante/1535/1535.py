#Números Casal-Solteirão-Solteirona

#a) Se um número é um número casal quadrado. 

#b) Se o número for casal quadrado então encontre esse 
# forma de expressá-lo.

#c) Descubra quantos números casal quadrado estão 
# dentro de um determinado intervalo (incluindo os 
# números das pontas).

# a * a - b * b = N

controle = False


while controle == False:
    a = 0
    b = 0
    try:
        n = input()
    except EOFError:
        controle == True
        break
    else:
        n = n.split()
        if len(n) == 1:
            n = int(n[0])

            t1 = int(n/2 - 4)
            t2 = int(n/2 + 4)

            for i in range(t1, t2):
                for j in range(t1, t2):
                    if ((i * i) - (j * j)) == n:
                        a = i
                        b = j
            if a == 0 and b == 0:
                if n % 2 == 0:
                    print('Bachelor Number.')
                else:
                    print('Spinster Number.')
            else:
                print(a, b)
        else:
            quantidade = 0
            for i in range(0, len(n)):
                n[i] = int(n[i])
            for z in range(n[0], n[1]+1):
                t1 = int(z/2 - 4)
                t2 = int(z/2 + 4)
                for i in range(t1, t2):
                    for j in range(t1, t2):
                        if ((i * i) - (j * j)) == n:
                            a = i
                            b = j
                if a == 0 and b == 0:
                    if n % 2 == 0:
                        quantidade += 1
            print(quantidade)
