'''
regra de negocio: C * F <= P

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). O arquivo de entrada contém três números inteiros C (1 ≤ C ≤ 1000), P (1 ≤ P ≤ 1000) e F (1 ≤ F ≤ 1000) representando respectivamente o número de competidores, a quantidade de folhas de papel especial compradas pela Diretora e a quantidade de folhas de papel especial que cada competidor deve receber.

Saída
Seu programa deve imprimir, na saída padrão, o caractere 'S' se a quantidade de folhas compradas pela Diretora é suficiente, ou o caractere 'N' caso contrário. Note que os caracteres devem ser letras maiúsculas.

'''

def main():
    C, P, F = input().split(' ')
    C, P, F = int(C), int(P), int(F)
    if C * F <= P:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
