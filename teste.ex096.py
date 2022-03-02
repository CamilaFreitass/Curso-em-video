def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}X{comp} é {a}m')


#PROGRAMA PRINCIPAL
print(' Controle de Terrenos ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)

