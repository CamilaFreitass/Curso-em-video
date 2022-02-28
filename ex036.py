#Empréstimo bancário para a compra de uma casa
vc = float(input('Qual o valor da casa?'))
sc = float(input('Qual o salário do comprador?'))
qa = float(input('Em quantos anos vai pagar?'))
prest = vc / (qa*12)
print('Valor da prestação é R${:.2f}!'.format(prest))
if prest > (sc*0.3):
    print('Empréstimo negado, valor da prestação excede 30% do salário!')
else:
    print('Tudo certo, empréstimo concedido!')



