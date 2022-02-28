n2 = 'S'
soma = cont = media = maior = menor = 0
while n2 not in 'N':
    n1 = int(input('Digite um número:'))
    n2 = str(input('Quer continuar? [S/N]')).upper()
    cont += 1
    soma = soma + n1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma/cont
print('Você digitou {}, a media foi {}, o maior número foi {} e o menor foi {}!'.format(cont, media, maior, menor))





