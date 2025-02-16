import subprocess
import argparse

# Função para rodar e testar o programa
def run_program(program, input_file, output_file):
    # Abrir os arquivos
    with open(input_file, 'r') as infile:
        input_data = infile.read()
    
    with open(output_file, 'r') as outfile:
        expected_output = outfile.read()
    
    # Rodar o programa passando o conteúdo de input.txt como entrada
    result = subprocess.run(['python', program], input=input_data, text=True, capture_output=True)
    
    # Verificar se a saída gerada é igual à saída esperada
    if result.stdout.strip() == expected_output.strip():
        print("Test passed!")
    else:
        print("Test failed!")
        print(f"Expected output:\n{expected_output}")
        print(f"Generated output:\n{result.stdout}")

# Configuração de argumentos da linha de comando
def main():
    parser = argparse.ArgumentParser(description="Testa um programa Python com input e output especificados.")
    parser.add_argument('program', help="O nome do programa Python a ser testado.")
    parser.add_argument('input', help="Arquivo de entrada (input.txt).")
    parser.add_argument('output', help="Arquivo de saída esperada (output.txt).")

    args = parser.parse_args()

    # Chamar a função de teste
    run_program(args.program, args.input, args.output)

if __name__ == "__main__":
    main()