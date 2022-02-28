pa = int(input('Qual o primeiro termo da PA?'))
razao = int(input('Qual a razão da PA?'))
decimo = pa + (10 - 1) * razao
for c in range(pa, decimo + razao, razao):
    print('{}'.format(c), end=' ')
print('ACABOU!')





