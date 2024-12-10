c = int( input() )

for i in range(0, c):
    dados = input().split()
    dados[1] = int( dados[1] )

    if dados[0] == 'Thor':
        print('Y')
    else:
        print('N')