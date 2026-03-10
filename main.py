import os
import shutil

pasta = "Downloads"

for arquivo in os.listdir(pasta):

    caminho_arquivo = os.path.join(pasta, arquivo)

    # ignora se for pasta
    if os.path.isdir(caminho_arquivo):
        continue

    arquivo_lower = arquivo.lower()

    if arquivo_lower.endswith(".pdf"):
        pasta_destino = os.path.join(pasta, "Documentos", "PDFs")

    elif arquivo_lower.endswith(".jpg") or arquivo_lower.endswith(".png"):
        pasta_destino = os.path.join(pasta, "Imagens")

    elif arquivo_lower.endswith(".mp3") or arquivo_lower.endswith(".wav"):
        pasta_destino = os.path.join(pasta, "Musicas")

    elif arquivo_lower.endswith(".mp4") or arquivo_lower.endswith(".avi"):
        pasta_destino = os.path.join(pasta, "Videos")

    else:
        continue

    os.makedirs(pasta_destino, exist_ok=True)

    shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))

print("Arquivos organizados com sucesso!")