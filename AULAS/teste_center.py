# Lista de meses de exemplo
meses = [str(i) for i in range(1, 70)]  # Gerando "1" a "12"

# Gerando a lista formatada
lista_formatada = []
juros = 0
for i, mes in enumerate(meses, start=1):
    juros += 30
    mes_formatado = mes.ljust(10)  # Preenchendo o mês com espaços até 10 caracteres
    valor = i * 100  # Só pra variar o valor, aumentando em cada iteração
    lista_formatada.append(f"{mes_formatado}{valor}   {juros}")

# Exibindo a lista final
for linha in lista_formatada:
    print(linha)
