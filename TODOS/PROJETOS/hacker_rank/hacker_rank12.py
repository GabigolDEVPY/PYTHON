def separa_ifen(line):
    texto_separado = line.split(" ")
    junto = "-".join(texto_separado)
    return junto
    

string = input()
result = separa_ifen(string)
print(result)
