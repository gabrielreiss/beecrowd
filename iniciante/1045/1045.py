#Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. 
# A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, 
# sempre escrevendo uma mensagem adequada:

#se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
#se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
#se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
#se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
#se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
#se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

dados = input().split()

for i in range(0,3):
    dados[i] = float(dados[i])

controle = 0
d1 = 0
d2 = 0

#while(controle == 0):

    #if c <= b <= a:
    #    controle = 1
    #elif b > a:
    #    d1 = b
    #    d2 = a
    #    a = d1
    #    b = d2
    #elif c > a:
    #    d1 = c
    #    d2 = a
    #    a = d1
    #    c = d2
    #elif c > b:
    #    d1 = c
    #    d2 = b
    #    b = d1
    #    c = d2

while(controle == 0):
    if dados[2] <= dados[1] <= dados[0]:
        controle = 1
    else:
        for i in range(0,2):
            if dados[i] < dados[i+1]:
                d1 = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = d1
            
a = dados[0]
b = dados[1]
c = dados[2]

if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')
if a==b==c:
    print('TRIANGULO EQUILATERO')
elif a==b or a==c or b==c:
    print('TRIANGULO ISOSCELES')