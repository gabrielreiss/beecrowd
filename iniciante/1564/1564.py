#Vai Ter Copa?
controle = False

while controle == False:
    try:
        n = input()
    except EOFError:
        break    
    else:
        n = int(n)
        if n == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')