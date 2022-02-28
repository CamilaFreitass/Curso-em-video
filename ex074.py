import random
numeros = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print('Os valores sorteados foram:', end='')
for cont in numeros:
    print(f' {cont} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')








