# casa 8 x 10
# 80 metros quadrados a casa

cont= False

casa = 80

while cont == False:
    dados = input().split()
    if dados == ['0']:
        cont = True
    else:
        a = int(dados[0])
        b = int(dados[1])
        c = int(dados[2])/100

        lado = ((a*b)/c)**(1/2)
        lado = int(lado)
        print(lado)