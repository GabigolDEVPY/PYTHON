lista = ["abriel", "bamdom", "carros", "dasa", "moto", "zelular"]


def busca_binaria(busca, array):
    ordenado = sorted(array)
    
    left_pointer = len(ordenado) - len(ordenado)
    right_pointer = len(ordenado) -1
    
    while left_pointer <= right_pointer:
        meio = ((left_pointer + right_pointer) // 2)      
        chute = ordenado[meio]
        
        if chute == busca:
            return meio
        
        elif chute > busca:
            right_pointer = meio - 1
            
        elif chute < busca:
            left_pointer = meio + 1
            
        else:
            print("não encontrado")    
            
result = busca_binaria("zelular", lista)
print(result)            