cont = False

while cont == False:
    n = int(input())
    if n == 0:
        cont = True
    else:
        m = []
        w, h = n, n
        m = [[0 for x in range(w)] for y in range(h)]

        for i in range(0, n):
            for j in range(0, n):
                m[i][j] = 2 ** (i+j)
        
        T = len(str(m[n-1][n-1]))
        for i in range(n):
            for j in range(n):
                m[i][j] = str(m[i][j])
                while len(m[i][j]) < T:
                    m[i][j] = ' ' + m[i][j]
            M = ' '.join(m[i])
        
            print(M)
        print()
