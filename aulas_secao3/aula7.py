texto = input('Digite um texto: ')
palavra_que_deseja_saber_mais = input('Digite a palavra que quer saber: ')

palavra_que_apareceu_mais = texto.count(palavra_que_deseja_saber_mais)

print(f'A palavra {palavra_que_deseja_saber_mais} apareceu {palavra_que_apareceu_mais} vezes')