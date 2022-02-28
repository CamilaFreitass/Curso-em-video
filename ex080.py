lista = []
cont = 0
for r in range(0, 5):
    n = int(input('Digite um valor:'))
    cont += 1
    if cont == 1 or n >= max(lista):
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
print(lista)

