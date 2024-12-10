a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

#é triangulo se o lado maior < outros dois lados

triangulo = 0

if a > b and a > c:
    if a <= b + c:
        triangulo = 1
elif b > a and b > c:
    if b <= a + c:
        triangulo = 1
elif c > a and c > b:
    if c <= a + b:
        triangulo = 1

perimetro = a+b+c
area = ((a+b)*c)/2

if triangulo == 1:
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    print('Area = {:.1f}'.format(area))