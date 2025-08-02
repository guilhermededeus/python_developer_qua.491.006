import os

limpar_tela = lambda: os.system("cls" if os.name == "nt" else "clear")
