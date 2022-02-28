from random import randint
from time import sleep
dicio = dict()
cont = 0
lista = []
while cont < 4:
    num = randint(1, 6)
    if num not in lista:
        lista.append(num)
        cont += 1
        dicio[f'Jogador {cont}'] = num
lista.sort()
print('Valores sorteados:')
sleep(2)
for c, v in dicio.items():
    print(f'O {c} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
sleep(1)
quant = 0
for i in sorted(dicio, key=dicio.get, reverse=True):
    quant += 1
    print(f'{quant}° lugar {i} com  {dicio[i]} ')
    sleep(1)



