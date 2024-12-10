#Eu fiz ao contrario

#se algarismo i é menor que algarismo i+1, 
#então é o valor i+1-i

romano = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

n = input()

#soma = sum([romano[i] for i in n])

soma = 0
for i in range(0, len(n)-1):
    if romano[ n[i] ] >= romano[ n[i+1] ]:
        soma += romano[ n[i] ]
        #print(romano[ n[i] ])
    else:
        soma -= romano[ n[i] ]
        #print(-romano[ n[i] ])
soma += romano[n[len(n)-1]]

print(soma)