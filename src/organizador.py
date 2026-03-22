import tkinter as tk
from tkinter import filedialog
import shutil
from pathlib import Path

CATEGORIAS = {
    "Imagens": [".jpg",".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Músicas": [".mp3", ".wav", ".aac", ".flac"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Código": [".py", ".js", ".html", ".css", ".json"],
}

def obter_categoria(extensao):
    extensao = extensao.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"

def organizar_pasta(caminho_pasta):
    pasta = Path(caminho_pasta)

    if not pasta.exists():
        print(f"Pasta não encontrada: {caminho_pasta}")
        return

    if not pasta.is_dir():
        print(f"O caminho informado não é uma pasta: {caminho_pasta}")
        return

    print(f"\n📂 Organizando: {pasta.resolve()}")
    print("=" * 50)

    movidos = 0
    ignorados = 0

    for arquivo in pasta.iterdir():
        if arquivo.is_dir() or arquivo.name.startswith("."):
            ignorados += 1
            continue

        categoria = obter_categoria(arquivo.suffix)

        destino_pasta = pasta / categoria
        destino_pasta.mkdir(exist_ok=True)

        destino_arquivo = destino_pasta / arquivo.name

        shutil.move(str(arquivo), str(destino_arquivo))
        print(f"{arquivo.name} -> {categoria}/")
        movidos += 1

    print("=" * 50)
    print(f"\n Concluído! {movidos} arquivo(s) organizado(s), {ignorados} ignorado(s).\n")

def main():
    print("iniciando...")
    print("=" * 50)
    print("Organizador Automático de Arquivos")
    print("=" * 50)

    root = tk.Tk()
    root.withdraw()

    caminho = filedialog.askdirectory(title="Escolha a pasta a organizar")

    if not caminho:
        print("\nNenhuma pasta selecionada. Encerrando...")
        return

    organizar_pasta(caminho)
if __name__ == "__main__":
    main()