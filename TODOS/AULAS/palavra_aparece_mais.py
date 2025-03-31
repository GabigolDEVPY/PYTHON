print('Vou contar quantas vezes a palavra apareceu!')
texto = input('Digite o texto: ').lower()
palavra = input('Digite a palavra que deseja: ')

palavra_apareceu = texto.count(palavra)
print(f'A palavra {palavra} apareceu {palavra_apareceu} vezes!')