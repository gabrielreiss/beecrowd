n = int(input())

texto = ''

fib = [0, 1]

if n > (len(fib)):
    texto += '0 1 '
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])
        texto += str(fib[i]) + ' '
else:
    for i in range(0,n):
        texto += str(fib[i]) + ' '

print(texto[:-1])
    