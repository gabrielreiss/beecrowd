h1, m1, h2, m2 = input().split()
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

if h1 == h2 and m1 == m2:
    print('O JOGO DUROU 24 HORA(S)')
elif h1 <= h2:
    if m2 >= m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h2-h1, m2-m1))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h2-h1, 60+m2-m1))
elif h1 >= h2:
    if m2 >= m1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24+h2-h1,m2-m1))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24+h2-h1,60+m2-m1))