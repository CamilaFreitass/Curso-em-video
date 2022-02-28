c = int(input('Digite um número para calcular seu fatorial:'))
# c = n1
f = 1
print('Calculando {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))






