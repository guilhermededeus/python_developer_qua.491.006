# Importando bibliotecas
from deep_translator import GoogleTranslator
import os

def traduzir_texto(texto):
    try:
        tradutor = GoogleTranslator(source="auto", target="pt")
        traducao = tradutor.translate(texto)
        return traducao
    except Exception as e:
        print(f"Erro ao traduzir o texto: {e}")
        return None

def abrir_arquivo(caminho_arquivo):
    try:
        if os.name == "nt":  # Windows
            os.startfile(caminho_arquivo)
        elif os.name == "posix": 
            os.system(f"xdg-open '{caminho_arquivo}'")
    except Exception as e:
        print(f"Não foi possível abrir o arquivo automaticamente: {e}")