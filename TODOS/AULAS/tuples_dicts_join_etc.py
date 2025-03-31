import os

directory = "/home/gabigordo/Downloads/PYTHON"
unir = os.path.join(directory,'dados.json')

def stri():
    return "eu"

print(unir)

lista_de_frutas = ["maçã", "banana", "laranja"]
string_final = ", ".join(lista_de_frutas)
print(string_final)

tupla_dee_numeros = (1, 2, 3)
string_numeros = "-".join(str(num) for num in tupla_dee_numeros)

print(string_numeros)


stt = stri().join(str(num) for num in tupla_dee_numeros)

print(stt)


names = ["Alice", "Bob", "Charlie"]
greetings = ["Hello", "Hi", "Hello"]
messages = [" How are you ?", "!", " Nice to meet you"]

completed_messages = [f"{greetings[i]} {name}{messages[i]}" for i, name in enumerate(names)]
print(completed_messages)
final_message = "\n".join(completed_messages)
print(final_message)


iii = ["Hi", "Hello", "Nice"]
jjj = ["gabriel", "gabi", "Me"]
ooo = [" Banana", " Strawberry", " Pineapple"]

fruti_list = [f"{iii[i]} {nome}{ooo[i]}" for i, nome in enumerate(jjj)]
sep_list_fruti = "\n".join(fruti_list)

print(fruti_list)

print(sep_list_fruti)


new_list = []

for i, nome in enumerate(jjj):
    new_list.append(f"{iii[i]} {nome}{ooo[i]}")
    
    
new_list_sep = "\n".join(new_list)    

print(new_list_sep)


produtos = [("Maçã", 2.5), ("Banana", 1.8), ("Laranja", 3.0)]

cabecalho = "Produto\tPreço"

linhas = [f"{produto[0]}\t{produto[1]:.2f}" for produto in produtos]

relatorio = "\n".join([cabecalho] + linhas)

print(relatorio)


print(f"{int(18):.3f}")

x = 5.6789
print("{:.3f}".format(x))


for p in produtos:
    print(f"{p[0]}\t{p[1]:.2f}")