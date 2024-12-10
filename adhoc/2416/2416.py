entrada = input()

treinamento_metros, comprimento_pista = map(int, entrada.split())

ponto_termino = treinamento_metros % comprimento_pista

print(ponto_termino)
