'''
Você reuniu então todas as categorias de colocações que as pessoas mais usam: 1, 3, 5, 10, 25, 50 e 100. Dada uma colocação K, diga o número da menor categoria que esta colocação pertence.
'''

n = int(input())

if n <= 1:
    print(f"Top 1")
elif n <= 3:
    print(f"Top 3")
elif n <= 5:
    print(f"Top 5")
elif n <= 10:
    print(f"Top 10")
elif n <= 25:
    print(f"Top 25")
elif n <= 50:
    print(f"Top 50")
elif n <= 100:
    print(f"Top 100")