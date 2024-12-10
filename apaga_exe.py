import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def delete_exe_files(start_path):
    """
    Remove arquivos com extensão .exe em um diretório e suas subpastas.

    Args:
        start_path (str): Caminho do diretório inicial.
    """
    lista_palavras = [".exe", ".class", ".pdb"]
    
    for extensao in lista_palavras:
        for root, dirs, files in os.walk(start_path):
            for file in files:
                if file.endswith(extensao):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        print(f"Arquivo deletado: {file_path}")
                    except Exception as e:
                        print(f"Erro ao deletar {file_path}: {e}")

delete_exe_files(BASE_DIR)