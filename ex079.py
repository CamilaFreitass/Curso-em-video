lista = []
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print(f'{lista}')
    else:
        print('Valor duplicado! Não vou adicionar...')
    p = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if p == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

