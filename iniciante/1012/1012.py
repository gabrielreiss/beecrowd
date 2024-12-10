linha = input().split()

a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

t = (a*c)/2

print('TRIANGULO: {:.3f}'.format(t))

pi = 3.14159

print("CIRCULO: {:.3f}".format(pi*c**2))

print('TRAPEZIO: {:.3f}'.format( ((a+b)*c)/2 ))

print("QUADRADO: {:.3f}".format(b**2))

print("RETANGULO: {:.3f}".format(a*b))