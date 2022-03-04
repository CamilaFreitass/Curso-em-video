from time import sleep
import random
lista = list()
par = list()

def sorteia():
    lista.append(random.randint(0, 100))
    lista.append(random.randint(0, 100))
    lista.append(random.randint(0, 100))
    lista.append(random.randint(0, 100))
    lista.append(random.randint(0, 100))
    print(lista)


def somapar():
    for valor in lista:
        if (valor % 2) == 0:
            par.append(valor)
        total = sum(par)
    print(total)

print(f'Sorteando 5 valores para lista: ', end='')
sleep(1)
sorteia()
sleep(1)
print(f'Somando os valores pares de {lista}, temos ', end='')
sleep(1)
somapar()
