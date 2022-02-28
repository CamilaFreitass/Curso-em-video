viage = int(input('Qual a distância da viagem em quilômetros?'))
if viage <= 200:
    valor = (0.5) * viage
    print('O preço da passagem é R${}'.format(valor))
else:
    valor2 = 0.45 * viage
    print('O preço da passagem é R${}'.format(valor2))


