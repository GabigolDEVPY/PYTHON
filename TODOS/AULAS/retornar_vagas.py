assentos = [
    {     
    "Assento": 1,
    "Situação": "Ocupado"
    },
    {     
    "Assento": 2,
    "Situação": "Livre"  
    },
    {     
    "Assento": 3,
    "Situação": "Livre"  
    },
    {     
    "Assento": 4,
    "Situação": "Ocupado"  
    },
    {     
    "Assento": 5,
    "Situação": "Ocupado"  
    }
    ]


def procurar_lugar(lista, vaga):
    atualizados = []
    for assento in lista:
        if assento["Assento"] == vaga and assento["Situação"] == "Livre":
            atualizados.append({"Assento": vaga, "Situação": "Ocupado"})
            print("Seu lugar foi marcado no assento", vaga)
            continue
        atualizados.append(assento)
        if assento["Situação"] == "Livre":
            print("Assento", assento["Assento"], "está vago")
            
    return atualizados    
    

lugares = procurar_lugar(assentos, 3) 
print(lugares)