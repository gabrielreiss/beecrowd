#Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível 
# segundo o esquema abaixo, da esquerda para a direita.  
# Em seguida conclua qual dos animais seguintes foi escolhido, 
# através das três palavras fornecidas.

#Entrada
#A entrada contém 3 palavras, uma em cada linha, 
# necessárias para identificar o animal segundo a figura acima, 
# com todas as letras minúsculas.

#Saída
#Imprima o nome do animal correspondente à entrada fornecida.

carac1 = input().lower()
carac2 = input().lower()
carac3 = input().lower()

if carac1 == 'vertebrado':
    if carac2 == 'ave':
        if carac3 == 'carnivoro':
            print('aguia')
        elif carac3 == 'onivoro':
            print('pomba') 
    elif carac2 == 'mamifero':
        if carac3 == 'onivoro':
            print('homem')
        elif carac3 == 'herbivoro':
            print('vaca')        
elif carac1 == 'invertebrado':
    if carac2 == 'inseto':
        if carac3 == 'hematofago':
            print('pulga')
        elif carac3 == 'herbivoro':
            print('lagarta')
    elif carac2 == 'anelideo':
        if carac3 == 'hematofago':
            print('sanguessuga')
        elif carac3 == 'onivoro':
            print('minhoca')


