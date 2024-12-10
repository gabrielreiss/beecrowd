#Matriz Quadrada I

#Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), 
# correspondente a ordem de uma matriz M de inteiros, 
# e construa a matriz de acordo com o exemplo abaixo.

#Entrada
#A entrada consiste de vários inteiros, um valor por linha, 
# correspondentes as ordens das matrizes a serem construídas. 
# O final da entrada é marcado por um valor de ordem 
# igual a zero (0).

#Saída
#Para cada inteiro da entrada imprima a matriz correspondente, 
# de acordo com o exemplo. Os valores das matrizes 
# devem ser formatados em um campo de tamanho 3 justificados 
# à direita e separados por espaço. Após o último 
# caractere de cada linha da matriz não deve haver 
# espaços em branco. Após a impressão de cada matriz 
# deve ser deixada uma linha em branco.

controle = False

while controle == False:
    n = int(input())
    if n == 0:
        controle = True
    else:
        m = []
        w, h = n, n;
        m = [[0 for x in range(w)] for y in range(h)]

        for i in range(0, n):
            for j in range(0, n):
                for z in range(0, n):
                    if i == 0:
                        m[i][j] = i + 1
                    elif j == 0:
                        m[i][j] = j + 1
                    elif i == (n-1):
                        m[i][j] = n-i
                    elif j == (n-1):
                        m[i][j] = n-j
                    elif i >= (z-1):
                        m[i][j] = z
                    elif j >= (z-1):
                         m[i][j] = z
        print(m)