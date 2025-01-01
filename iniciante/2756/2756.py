vetor = ['A', 'B', 'C', 'D', 'E']

a = 7; b = -1
for i in range(5):
    if i == 0:
        print(f'{" " * a}{vetor[i]}')
    else:
        print(f'{" " * a}{vetor[i]}{" "* b}{vetor[i]}')
    a -= 1; b +=2;

a = 4; b = 5;
for i in range(4):
    if i == 3:
        print(f'{" " * a}{vetor[3-i]}')
    else:
        print(f'{" " * a}{vetor[3-i]}{" "* b}{vetor[3-i]}')
    a += 1; b -=2;
