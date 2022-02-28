soma = cont = menor = quant = 0
barato = ' '
while True:
    produto = str(input('Produto:')).strip().upper()
    preço = int(input('Preço: R$'))
    quant += 1
    soma += preço
    if preço > 1000:
        cont += 1
    if quant == 1 or preço < menor:
        menor = preço
        barato = produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
print('Fim!')
print(f'O total gasto na compra foi: R${soma:.2f}')
print(f'Temos {cont} produtos que custam mais de R$ 1000')
print(f'O produto mais barato foi {barato} e custou {menor:.2f}')
























