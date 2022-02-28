n1 = int(input('Digite um valor para a posição 0:'))
n2 = int(input('Digite um valor para a posição 1:'))
n3 = int(input('Digite um valor para a posição 2:'))
n4 = int(input('Digite um valor para a posição 3:'))
n5 = int(input('Digite um valor para a posição 4:'))

lista = [n1, n2, n3, n4, n5]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for y, r in enumerate(lista):
    if r == max(lista):
        print(f'{y}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for y, r in enumerate(lista):
    if r == min(lista):
        print(f'{y}... ', end='')




