# 📁 Organizador Automático de Arquivos

Script em Python que organiza automaticamente os arquivos de uma pasta, separando-os em subpastas por tipo.

## O que ele faz

Antes de rodar:
```
Downloads/
├── foto_viagem.jpg
├── trabalho_escola.pdf
├── musica.mp3
└── video_aula.mp4
```

Depois de rodar:
```
Downloads/
├── Imagens/
│   └── foto_viagem.jpg
├── Documentos/
│   └── trabalho_escola.pdf
├── Músicas/
│   └── musica.mp3
└── Vídeos/
    └── video_aula.mp4
```

## Categorias suportadas

| Categoria | Extensões |
|-----------|-----------|
| Imagens | .jpg, .png, .gif, .webp |
| Documentos | .pdf, .docx, .xlsx, .txt |
| Vídeos | .mp4, .mov, .avi, .mkv |
| Músicas | .mp3, .wav, .aac, .flac |
| Compactados | .zip, .rar, .7z |
| Código | .py, .js, .html, .css |

## Como usar

1. Clone o repositório
2. Execute o script
3. Escolha a pasta na janela que abrir

## Tecnologias

- Python 3.8+
- tkinter
- shutil
- pathlib