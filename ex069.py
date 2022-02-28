cont18 = contH = contM = 0
while True:
    idade = int(input('IDADE:'))
    if idade > 18:
         cont18 += 1
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input('SEXO: [M/F]')).upper().strip()[0]
        if sexo == 'M':
            contH += 1
    if sexo == 'F' and idade < 20:
        contM += 1
    n1 = ' '
    n1 = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if n1 == 'N':
        break
print('Fim do Programa!')
print(f'Total de pessoas com mais de 18: {cont18}')
print(f'Ao todo temos {contH} homens cadastrados')
print(f'Total de mulheres com menos de 20: {contM}')


































