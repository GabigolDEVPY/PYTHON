
despesas = [
    {
        "item": "carro",
    "valor": 1500,
    },    
    {
        "item": "moto",
    "valor": 1200,
    },    
    {
        "item": "casa",
    "valor": 1100   
    }  
]

def calculo_despesas(salario, lista_despesas, desconto):
    total_despesas = 0
    
    for _ in lista_despesas:
        total_despesas += _["valor"]
        
    total_despesas = total_despesas - ((total_despesas / 100) * desconto)
    total = (salario - total_despesas)
    print(total)    
    
calculo_despesas(5000, despesas, 10)

