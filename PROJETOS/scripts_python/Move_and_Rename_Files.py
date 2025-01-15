import shutil

# Caminho do arquivo original e destino
origem = "caminho_para_arquivo/arquivo.txt"
destino = "caminho_para_nova_pasta/novo_nome.txt"

# Move e renomeia o arquivo
shutil.move(origem, destino)
print("Arquivo movido e renomeado com sucesso.")
