def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * (taxa / 100))
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * (taxa /100))
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço /2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(num, taxa=0, taxa2=0):
    print('  RESUMO DO VALOR  ')
    print(f'Preço analisado: \t{moeda(num):>3}')
    print(f'Dobro do preço: \t{dobro(num, True):>3}')
    print(f'Metade do preço: \t{metade(num, True):>3}')
    print(f'{taxa}% de aumento: \t{aumentar(num,taxa, True):>3}')
    print(f'{taxa2}% de redução: \t{diminuir(num, taxa2, True):>3}')
