#Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, 
#2.0 4.0 7.5 8.0 6.4
dados = input().split()

for i in range(0,len(dados)):
    dados[i] = float(dados[i])

# correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, 
pesos = [2, 3, 4, 1]

total = 0

for i in range(0, len(pesos)): #problemas aqui
    total = total + pesos[i]*dados[i]

media = total/10
print(media)

# respectivamente, para cada uma destas notas e mostre esta média acompanhada pela 
# mensagem "Media: ". 
print('Media: {:.1f}'.format(media))

# Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". 
if media >= 7.0:
    print('Aluno aprovado.')

# Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". 
if media < 5.0:
    print('Aluno reprovado.')

# Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, 
# o programa deve imprimir a mensagem "Aluno em exame.".
if 5 <= media <= 6.9:
    print('Aluno em exame.')
else:
    #No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida 
    # pelo aluno. 
    exame = float(input())

    #Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. 
    print('Nota do exame: {}'.format(exame))

    # Recalcule a média (some a pontuação do exame com a média anteriormente calculada e 
    # divida por 2).
    nova_media = (media + exame)/2
    # e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) 
    # ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 
    # Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na 
    # última linha uma mensagem "Media final: " seguido da média final para esse aluno.

    if nova_media >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {}'.format(nova_media))
    else:
        print('Aluno reprovado.')
        print('Media final: {}'.format(nova_media))


#Entrada
#A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

#Saída
#Todas as respostas devem ser apresentadas com uma casa decimal. 
# As mensagens devem ser impressas conforme a descrição do problema. 
# Não esqueça de imprimir o enter após o final de cada linha, caso contrário 
# obterá "Presentation Error".



