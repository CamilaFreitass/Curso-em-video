lista = []
listap = []
listai = []
while True:
    nume = int(input('Digite um número:'))
    lista.append(nume)
    if (nume % 2) == 0:
        listap.append(nume)
    else:
        listai.append(nume)
    perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listap}')
print(f'A lista de ímpares é {listai}')
