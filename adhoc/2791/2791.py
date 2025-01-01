'''
Entrada = [c1 c2 c3 c4]

ci = 1 feijao estava no copo numero i
ci = 0 copo vazio

Saída
Escreva na saída uma linha contendo um inteiro entre 1 e 4, correspondendo à posição onde o feijão estava.
'''

vetor = input().split(' ')

posicao = 0

for i in range(4):
    if vetor[i] == '1':
        posicao = i + 1
        
print(posicao)
