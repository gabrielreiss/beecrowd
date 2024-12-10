#cilindro
#pi = 3.14

controle = False
pi = 3.14
while controle == False:
    try:
        v = float(input())
        d = float(input())
    except EOFError:
        break    
    else:
        altura = v / ( pi * ((d/2)**2) )

        area = pi * ((d/2) ** 2)

        print('ALTURA = {:.2f}'.format(altura))
        print('AREA = {:.2f}'.format(area))