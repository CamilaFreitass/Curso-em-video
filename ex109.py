def aumentar(num=0, taxa=0, moeda=False):
    aum = num + (num * (taxa/100))
    if moeda:
       print(f'Aumentando {taxa}%, temos R${aum:.2f}'.replace('.', ','))
    else:
        print(f'Aumentando {taxa}%, temos {aum:.2f}')
    return aum


def diminuir(num=0, taxa=0, moeda=False):
    dim = num - (num * (taxa/100))
    if moeda:
        print(f'Reduzindo {taxa}%, temos R${dim:.2f}'.replace('.', ','))
    else:
        print(f'Reduzindo {taxa}%, temos {dim:.2f}')
    return dim


def metade(num=0, moeda=False):
    met = num / 2
    if moeda:
        print(f'A metade de R${num:.2f} é R${met:.2f}'.replace('.', ','))
    else:
        print(f'A metade {num:.2f} é {met:.2f}')
    return met


def dobro(num=0, moeda=False):
    dob = num * 2
    if moeda:
        print(f'O dobro de R${num:.2f} é R${dob:.2f}'.replace('.', ','))
    else:
        print(f'O dobro de {num:.2f} é {dob:.2f}')
    return dob


# preço = float(input('Digite o preço: R$ '))
# aumentar(preço, 10, moeda=True)
# diminuir(preço, 13, moeda=True)
# metade(preço, moeda=True)
# dobro(preço, moeda=True)





