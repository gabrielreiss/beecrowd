dados = input().split()

s = int(dados[0]) # hora saida
t = int(dados[1]) # tempo viagem
f = int(dados[2]) # fuso horario

r = s + t + f

if r > 24:
    r -= 24
elif r < 0:
    r += 24
print(r)