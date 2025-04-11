import os

# Pega o caminho onde este arquivo atual esta sendo executado
DIRETORIOARQUIVO = os.path.abspath(__file__)

# Pega o diretório de onde este arquivo está sendo executado porém sem o nome do arquivo em si!!
Only_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


print(DIRETORIOARQUIVO)
print(Only_DIRECTORY)

# essa função uni o caminho retornado pela variável Only_DIRECTORY que é "c:\Users\gabig\Downloads\PYTHON" mais a STR que foi passada 'lista_palavras.json' 
# Assim ARQUIVO_PALAVRAS retorna "c:\Users\gabig\Downloads\PYTHON\lista_palavras.json"
ARQUIVO_PALAVRAS = os.path.join(Only_DIRECTORY, 'lista_palavras.json')


print(ARQUIVO_PALAVRAS)