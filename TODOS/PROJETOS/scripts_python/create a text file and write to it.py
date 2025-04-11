# create a text file and write to it
import os

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(DIRECTORY, "arquivo_exemplo.txt")

with open(FILE, "w") as file:
    file.write("Linha 1: Este é um exemplo de texto.\n")
    file.write("Linha 2: Este é outro exemplo de texto.")
