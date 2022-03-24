def leiaDinheiro(num):
    leia = input('Digite o preço: R$')
    while True:
        if num != leia.isnumeric():
            print(f'ERRO: {leia} é um preço inválido!')
            leia
        else:
            break