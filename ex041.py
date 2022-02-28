from datetime import date
nasc = int(input('Qual o seu ano de nascimento?'))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e sua categoaria é JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos e sua categoria é SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER'.format(idade))

