preço = float(input('Qual o preço?'))
pagamento = int(input('''
[1] Dinheiro à vista
[2] Cheque à vista 
[3] Cartão à vista
[4] Cartão 2x
[5] Cartão 3x ou mais
Digite o número da forma de pagamento:'''))
if pagamento == 1 or pagamento == 2:
    print('Com desconto de 10% o preço a ser pago é R${}!'.format(preço-(preço*0.1)))
elif pagamento == 3:
    print('Com 5% de desconto o preço a ser pago é R${}!'.format(preço-(preço*0.05)))
elif pagamento == 4:
    print('O preço a ser pago é R${}!'.format(preço))
elif pagamento == 5:
    print('Com 20% de juros o preço a ser pago é R${}!'.format(preço+(preço*0.2)))
else:
    print('Alternativa inválida, tente novamente!')


