from functools import reduce

itens = [
    {"nome": "iPhone 15 Pro Max", "preco": 9999.99},
    {"nome": "Notebook Gamer", "preco": 7999.90},
    {"nome": "Fone Bluetooth", "preco": 199.99},
    {"nome": "Mouse RGB", "preco": 149.90},
    {"nome": "Cadeira Gamer", "preco": 1299.00},
    {"nome": "Teclado Mecânico", "preco": 349.90},
    {"nome": "Monitor 4K", "preco": 2199.99},
    {"nome": "Echo Dot (Alexa)", "preco": 399.00},
    {"nome": "Placa de Vídeo RTX 4090", "preco": 12999.00},
    {"nome": "Gabinete com LED", "preco": 599.90}
]


soma = reduce(lambda x, y: x + y['preco'], itens, 0)


print(soma)
