controle = False
while controle == False:
    try:
        n = input()
    except EOFError:
        break    
    else:
        n = int(n)
        dados = input().split()
        classificacao = 1
        for i in range(0, n):
            dados[i] = int(dados[i])
            if classificacao < 3:
                if 10 <= dados[i] < 20:
                    classificacao = 2
                elif dados[i] >= 20:
                    classificacao = 3
        print(classificacao)
        