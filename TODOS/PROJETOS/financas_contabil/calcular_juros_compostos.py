def calculo(valor_inicial, valor_mensal_adicionado, porcentagem_juros_mensais, numero_meses):
    
    total = valor_inicial
    for _ in range(numero_meses):
        total += (total / 100) * porcentagem_juros_mensais
        
        total += valor_mensal_adicionado
    print(f" total final {total:.2f}")

calculo(1000, 200, 0.05, 12)