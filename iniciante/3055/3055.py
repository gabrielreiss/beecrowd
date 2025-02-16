'''
A primeira linha contém um número inteiro A, indicando a nota de uma prova. A segunda linha contém um número inteiro M, indicando a média entre as duas notas das provas.
'''

def reverse_mean(a, m):
    return (m * 2) - a

def main():
    a = int(input())
    m = int(input())
    print(reverse_mean(a, m))

if __name__ == "__main__":
    main()

