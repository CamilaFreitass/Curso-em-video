import random
n2 = random.randint(0, 10)
print('Advinhe até acertar o número entre 0 e 10 escolhido pelo computador')
n1 = int(input('Digite seu palpite:'))
totn1 = 1
while n1 != n2:
    if n2 > n1:
        print('Mais... tente outra vez!')
    else:
        print('Menos... tente outra vez!')
    n1 = int(input(' Digite seu palpite: '))
    totn1 += 1
print('Parabéns, você acertou! O número de tentativas foram {}!'.format(totn1))













