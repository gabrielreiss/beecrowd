a, b = input().split()
a = int(a)
b = int(b)

if a == b:
    print('O JOGO DUROU 24 HORA(S)')
elif a < b:
    print('O JOGO DUROU {} HORA(S)'.format(b-a))
elif a > b:
    print('O JOGO DUROU {} HORA(S)'.format(24-a+b))