while True:
    n = int(input('Digite um número para ver a tabuada:'))
    if n < 0:
        break
    for tabu in range(1, 11):
        print(f'{n} X {tabu:2} = {n*tabu}')
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
