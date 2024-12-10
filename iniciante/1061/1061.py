#Pedrinho está organizando um evento em sua Universidade. 
# O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. 
# O problema é que Pedrinho quer calcular o tempo que o evento vai durar, 
# uma vez que ele sabe quando inicia e quando termina o evento.

#Sabendo que o evento pode durar de poucos segundos a vários dias, 
# você deverá ajudar Pedrinho a calcular a duração deste evento.

#Entrada
#Como entrada, na primeira linha vai haver a descrição “Dia”, 
# seguido de um espaço e o dia do mês no qual o evento vai começar. 
# Na linha seguinte, será informado o momento no qual o evento vai iniciar, 
# no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra 
# informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

#Saída
#Na saída, deve ser apresentada a duração do evento, no seguinte formato:

#W dia(s)
#X hora(s)
#Y minuto(s)
#Z segundo(s)

#Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

#Exemplo de Entrada	Exemplo de Saída
#Dia 5
#08 : 12 : 23
#Dia 9
#06 : 13 : 23

#3 dia(s)
#22 hora(s)
#1 minuto(s)
#0 segundo(s)

dia1 = input().split()
d1 = int(dia1[1])

hora1 = input().split()
h1 = int(hora1[0])
m1 = int(hora1[2])
s1 = int(hora1[4])

dia2 = input().split()
d2 = int(dia2[1])

hora2 = input().split()
h2 = int(hora2[0])
m2 = int(hora2[2])
s2 = int(hora2[4])

dia = 0
hora = 0
minuto = 0
segundo = 0

if s2 < s1:
    segundo = 60 + m2 - m1
    minuto -= 1
else:
    segundo = m2 - m1

if (m2 - minuto) < m1:
    hora -= 1
    minuto = minuto + 60 + m2 -m1
else:
    minuto = minuto + m2 - m1

if h2 < h1:
    dia -= 1
    hora = hora + 24 + h2 -h1
else:
    hora = hora + h2 - h1

dia = dia + d2 - d1

print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(hora))
print('{} minuto(s)'.format(minuto))
print('{} segundo(s)'.format(segundo))