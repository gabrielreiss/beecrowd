controle = False
senha = '2002'

while controle == False:
    texto = input()
    if texto == senha:
        print('Acesso Permitido')
        controle = True
    else:
        print('Senha Invalida')