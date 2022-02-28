lista = []
pares = []
impares = []
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}° valor:'))
    if (n % 2) == 0:
        pares.append(n)
    else:
        impares.append(n)
lista.append(pares[:])
lista.append(impares[:])
print('-='*40)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitadi foram:{lista[1]}')


