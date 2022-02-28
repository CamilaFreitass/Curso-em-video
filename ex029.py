vel = int(input('Qual a velocidade que o carro está?'))
multa = (vel-80) * 7
if vel <= 80:
    print('Está dentro do limite de velocidade!')
else:
    print('Está acima do limite de velocidade, vai pagar uma multa de R${}.'.format(multa))

