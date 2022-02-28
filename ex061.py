pa = int(input('Qual o primeiro termo da PA?'))
razao = int(input('Qual a razão da PA?'))
termo = pa
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
