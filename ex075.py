cont = par = 0
n1 = int(input('Digite o primeiro valor:'))
if n1 == 9:
    cont += 1
n2 = int(input('Digite o segundo valor:'))
if n2 == 9:
    cont += 1
n3 = int(input('Digite o terceiro valor:'))
if n3 == 9:
    cont += 1
n4 = int(input('Digite o quarto valor:'))
if n4 == 9:
    cont += 1
valores = (n1,n2,n3,n4)

print(f'O valor 9 apareceu {cont}')
if 3 in valores:
    print(f'O valor 3 apareceu {valores.index(3)+1}°')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')






