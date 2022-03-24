import ex109


preço = float(input('Digite o preço: R$'))
ex109.aumentar(preço, 10, moeda=True)
ex109.diminuir(preço, 13, moeda=True)
ex109.metade(preço, moeda=True)
ex109.dobro(preço, moeda=True)

# print(f'A metade de {preço} é {ex109.metade(preço)}')
# print(f'O dobro de {preço} é {ex109.dobro(preço)}')
# print(f'Aumentando 10%, temos {ex109.aumentar(preço)}')
# print(f'Reduzindo 13% temos {ex109.diminuir(preço)}')
#print(f'{ex109.moeda(preço)}')
