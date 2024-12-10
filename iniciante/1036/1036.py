#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente 
# “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

a = float(input())
b = float(input())
c = float(input())
r1 = float()
r2 = float()

delta = b**2 - 4*a*c

if 2*a == 0 or delta<0:
    print("Impossivel calcular")
else:
    r1 = (-b + delta ** (1/2))/(2*a)
    r2 = (-b - delta ** (1/2))/(2*a)

    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))



