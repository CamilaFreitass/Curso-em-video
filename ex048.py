soma = 0
cont = 0
for som in range(1, 501, 2):
    if (som % 3) == 0:
        soma = soma + som
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))







