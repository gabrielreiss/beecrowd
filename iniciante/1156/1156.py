s = 1

numerador = 3
denominador = 2

while numerador <= 39:
    s += (numerador / denominador) 
    numerador += 2
    denominador *= 2

print('{:.2f}'.format(s))