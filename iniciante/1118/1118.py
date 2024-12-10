#Escreva um programa para ler as notas da primeira e 
# a segunda avaliação de um aluno. 
# Calcule e imprima a média semestral. 
# O programa só deverá aceitar notas válidas 
# (uma nota válida deve pertencer ao intervalo [0,10]).
# Cada nota deve ser validada separadamente.

novo_calculo = 1

while novo_calculo == 1:

    notas_validas = 0
    notas = 0
    soma = 0

    while notas_validas < 2:
        #if notas_validas == 2:
        #else:
        notas = float(input())
        if 0 <= notas <= 10:
            soma += notas
            notas_validas += 1
        else:
            print('nota invalida')

    media = soma / notas_validas
    print('media = {:.2f}'.format(media))
    #No final deve ser impressa a mensagem “novo calculo 
    # (1-sim 2-nao)”, solicitando ao usuário que informe 
    # um código (1 ou 2) indicando se ele deseja ou não 
    # executar o algoritmo novamente, 
    # (aceitar apenas os código 1 ou 2). 
    # Se for informado o código 1 deve ser repetida a 
    # execução de todo o programa para permitir um 
    # novo cálculo, caso contrário o programa 
    # deve ser encerrado.

    nv = 0
    while nv == 0:
        print('novo calculo (1-sim 2-nao)')
        opcao = int(input())
        if opcao == 2:
            novo_calculo = 2
            nv = 1
        elif opcao == 1:
            novo_calculo = 1
            nv = 1
        else:
            nv = 0

#Entrada
#O arquivo de entrada contém vários valores reais, 
# positivos ou negativos. Quando forem lidas duas notas
#  válidas, deve ser lido um valor inteiro X . 
# O programa deve parar quando o valor lido 
# para este X for igual a 2.

#Saída
#Se uma nota inválida for lida, 
# deve ser impressa a mensagem “nota invalida”. 
# Quando duas notas válidas forem lidas, 
# deve ser impressa a mensagem “media = ” seguido do 
# valor do cálculo.

#Antes da leitura de X deve ser impressa a 
# mensagem "novo calculo (1-sim 2-nao)" e esta 
# mensagem deve ser apresentada novamente se o 
# valor da entrada padrão para X for menor do 
# que 1 ou maior do que 2, conforme o exemplo abaixo.

#A média deve ser impressa com dois dígitos após 
# o ponto decimal.