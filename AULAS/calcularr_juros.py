def calcular_juros(valor_inicial, taxa_juros, tipo_juros, valor_investido_meses, meses, anual_ou_mensal):
    if anual_ou_mensal == "Anos":
        meses = (meses * 12) 
    if tipo_juros == "Anual":
        valor_juros = 0
        valor_final = valor_inicial
        taxa_juros = (1 + taxa_juros / 100) ** (1 / 12) - 1
        for _ in range(meses):
            juros = valor_final * taxa_juros
            valor_juros += juros
            valor_final += juros 
            valor_final += valor_investido_meses
    else:
        valor_juros = 0
        valor_final = valor_inicial        
        for _ in range(meses):
            juros = (valor_final / 100)  * taxa_juros
            valor_juros += juros
            valor_final += juros 
            valor_final += valor_investido_meses
    print(valor_final)
        
    
calcular_juros(1000, 1, "Mensal", 300, 12, "Meses") 


    