n = int(input())

for i in range(0, n):
    fib = [0, 1]
    x = int(input())
    if x > 1:
        for j in range(2, x+1):
            fib.append(fib[j-2]+fib[j-1])
    print('Fib({}) = {}'.format(x,fib[x]))