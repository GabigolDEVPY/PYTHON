from collections import namedtuple

Carta = namedtuple("carta", ["valor", "naipe"])
as_espadas = Carta("A", "H")
print(as_espadas)
print(as_espadas.naipe)
print(as_espadas.valor)

for valor in as_espadas:
    print("valorrrr", valor)