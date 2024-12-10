#Se em algum momento ela assumir a posição -1 ou a posição N, ela cairá do tronco! 

#P e dá um passo para a direita, ela assumirá a posição P+1
#Se o passo for para a esquerda, ela assumirá a posição P-1.
#Se em algum momento ela assumir a posição -1 ou a posição N, ela cairá do tronco! Um passo leva um segundo para ser completado, 
#e a formiga sempre está se movendo.

#Considerando que a formiga fará sempre a pior sequência 
#de passos possível, escolha uma posição inicial de 
#modo que maximize o tempo em que a formiga permaneça 
#no tronco. Imprima este tempo.

#Para cada caso, imprima o tempo máximo que a 
#formiguinha pode ficar no tronco.

t = int(input())

count1 = 0
count2 = 0

for i in range(0, t):
    d = int(input())
    d1 = d//2
    d2 = d//2
    while d1 > 0:
        d1 -= 1
        count1 += 1
    while d2 < d:
        d2 += 1
        count2 += 1
    
    if d1 < d2:
        print(count1)
    else:
        print(count2)