x = int(input())
z = []

cont = False

while cont == False:
    z.append(int(input()))
    if z[-1] > x:
        cont = True


soma = 0
cont2 = 0
while soma < z[-1]:
    if (soma + (cont2+1)) <= z[-1]:
        cont2 += 1
    soma += cont2

print(soma, cont2)