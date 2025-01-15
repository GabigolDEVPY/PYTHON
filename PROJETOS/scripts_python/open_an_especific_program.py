import subprocess

def abrir_programa(caminho_executavel):
    subprocess.Popen([caminho_executavel])

# Exemplo: abre o bloco de notas
abrir_programa("C:\\Windows\\System32\\notepad.exe")
