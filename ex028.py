import random
n1 = int(input('Qual foi o número escolhido pelo computador entre 0 e 5?'))
n2 = random.randint(0,5)
print('O número escolhido pelo computador foi {}'.format(n2))
if n1 == n2:
    print('Parabéns, você venceu!')
else:
    print('Que pena, você perdeu!')









