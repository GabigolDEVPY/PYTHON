def is_valid_number(peso):
    """Verifica se a entrada é um número válido (positivo ou negativo)."""
    try:
        float(peso)  # Tenta converter a entrada para float
        return True
    except ValueError:
        return False

def calcular_media_pesos():
    """Calcula e imprime a média de pesos informados pelo usuário.
    
    O usuário pode inserir pesos até decidir sair digitando 'sair'.
    A média é calculada e exibida se pelo menos um peso foi informado.
    """
    soma = 0
    quantidade = 0

    while True:
        peso = input('Digite [sair] se o número de pesos está ok ou informe o peso: ')
        
        if peso.lower() == 'sair':
            if quantidade > 0:
                media = soma / quantidade
                print(f'\nA média dos pesos é: {media:.2f}')
            else:
                print("\nNenhum peso foi informado.")
            break

        # Verifica se a entrada é um número válido
        if not is_valid_number(peso) or (float(peso) < 0):
            print('Digite um número válido.')  # Mensagem clara para entradas inválidas
            continue

        peso = float(peso)  # Tenta converter a entrada para float
        soma += peso  # Adiciona o peso à soma total
        quantidade += 1  # Aumenta a quantidade de pesos informados
        print(f'Soma atual dos pesos: {soma:.2f}')  # Mensagem de soma ajustada

# Chamada da função para executar o código
calcular_media_pesos()
