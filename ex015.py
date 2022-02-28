n1 = float(input('Quantos Km o carro percorreu?'))
n2 = float(input('Por quantos dias o carro foi alugado?'))
print('O carro percorreu {}Km e foi alugado por {} dias. Isso equivale a R${}!'.format(n1, n2, n1 * 0.15 + n2 * 60))
