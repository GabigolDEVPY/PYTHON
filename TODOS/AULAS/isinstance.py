lista = ["s", 1, 1.1, {1, 2}, True, [1, 2, 3], ()]

for indice, item in enumerate(lista):
    if isinstance(item, str):
        print(f'{indice}: {item} Is a STR')
    elif isinstance(item, (int, float)):
        print(f'{indice}: {item} Is a Number')
    elif isinstance(item, list):
        print(f'{indice}: {item} Is a list')
    elif isinstance(item, tuple):
        print(f'{indice}: {item} Is a Tuple')
    elif isinstance(item, bool):
        print(f'{indice}: {item} Is a Bool')
    elif isinstance(item, set):
        print(f'{indice}: {item} Is a SET')
    else:
        print('OUTRO')