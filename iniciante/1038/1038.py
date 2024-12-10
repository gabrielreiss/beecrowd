precos = [4, 4.5, 5, 2, 1.5]

dados = input().split()

cod = int(dados[0])
qnt = int(dados[1])

total = float(precos[cod-1])*qnt


print('Total: R$ {:.2f}'.format(total))