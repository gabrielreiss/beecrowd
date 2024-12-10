controle = 0
alcool = 0
gasolina = 0
diesel = 0


while (controle) == 0:
    a = int(input())
    
    if a == 1:
        alcool += 1
    elif a == 2:
        gasolina += 1
    elif a == 3:
        diesel += 1
    elif a == 4:
        controle = 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))