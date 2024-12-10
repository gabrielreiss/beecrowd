import os
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TARGET_DIR = os.path.join(BASE_DIR, 'iniciante')

arquivos = [f for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f))]

for arquivo in arquivos:
    nome_pasta = os.path.splitext(arquivo)[0]
    caminho_pasta = os.path.join(TARGET_DIR, nome_pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    caminho_arquivo = os.path.join(TARGET_DIR, arquivo)
    novo_caminho = os.path.join(caminho_pasta, arquivo)
    shutil.move(caminho_arquivo, novo_caminho)

