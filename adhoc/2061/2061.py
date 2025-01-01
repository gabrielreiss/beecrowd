'''
clicar em propaganda -> apaga aba sem abrir outra
fecha aba -> abre duas abas

inputs numero inicial sequencia de ações
fechou ou clicou

pergunta: quantas abas sobraram
'''
    
class Browser:
    def __init__(self, abas:int):
        self.abas = abas
    
    def acao(self, acoes:str):
        match acoes:
            case "clicou":
                self.abas -= 1
            case "fechou":
                self.abas += 1

def input_dados():
    string_input = input()
    abas_inicial, sequencia = string_input.split(' ')
    abas_inicial = int(abas_inicial)
    sequencia = int(sequencia)
    
    if abas_inicial < 0:
        print("ERRO: Abas_inicial menor que zero.")
        return 0, 0
    if sequencia > 500:
        print("ERRO: Muitas ações.")
        return 0, 0
    if sequencia < 0:
        print("ERRO: Ações negativas.")
        return 0, 0
    return abas_inicial, sequencia

def main():
    abas_inicial, sequencia = input_dados()
    
    browser = Browser(abas= abas_inicial)
    
    while sequencia !=0:
        acoes = str(input())
        browser.acao(acoes = acoes)
        sequencia -= 1
        
    return print(browser.abas)

if __name__ == "__main__":
    main()
