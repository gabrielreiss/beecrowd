t = int(input())

r = []

for i in range(0, t):
    dados = input().split()

    if dados[0] == dados[1]:
        r.append('De novo!')
    elif dados[0] == 'tesoura' and dados[1] == 'papel':
        r.append('Bazinga!')
    elif dados[0] == 'papel' and dados[1] == 'pedra':
        r.append('Bazinga!')
    elif dados[0] == 'pedra' and dados[1] == 'lagarto': 
        r.append('Bazinga!')
    elif dados[0] == 'lagarto' and dados[1] == 'Spock': 
        r.append('Bazinga!')
    elif dados[0] == 'Spock' and dados[1] == 'tesoura': 
        r.append('Bazinga!')
    elif dados[0] == 'tesoura' and dados[1] == 'lagarto':  
        r.append('Bazinga!')
    elif dados[0] == 'lagarto' and dados[1] == 'papel':  
        r.append('Bazinga!')
    elif dados[0] == 'papel' and dados[1] == 'Spock': 
        r.append('Bazinga!')
    elif dados[0] == 'Spock' and dados[1] == 'pedra':   
        r.append('Bazinga!')
    elif dados[0] == 'pedra' and dados[1] == 'tesoura':  
        r.append('Bazinga!')
    else:
        r.append('Raj trapaceou!')

for i in range(0, t):
    print('Caso #{}: {}'.format(i+1, r[i]))