def troca_letra(palavra, posicao, letra):
    nova_palavra = list(palavra)
    nova_palavra[posicao] = letra
    string = "".join(nova_palavra)
    return string

if __name__ == '__main__':
    palavra = input()
    i, c = input().split() 
    result = troca_letra(palavra, int(i), c)      
    print(result)      
            