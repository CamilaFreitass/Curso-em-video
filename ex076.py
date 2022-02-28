listagem = ('Livro', 34.90,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Compasso', 9.99,
            'Transferidor', 4.20,
            'Estojo', 25.00,
            'Caderno', 15.90,
            'Borracha', 2.00,
            'Lápis', 1.75)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS"}')
print('-'*40)
for posicao in range (0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem [posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
