salário = float(input('Qual o valor do seu salário?'))
aumento = salário * 0.10 if salário > 1250 else salário * 0.15
novosal = aumento + salário
print('O valor do seu aumento é R${} e você passará a ganhar R${}'.format(aumento, novosal))



