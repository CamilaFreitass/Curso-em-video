print('-=-'*20)
print('Vamos jogar PAR ou ÍMPAR')
print('-=-'*20)
import random
n2 = random.randint(0, 10)
cont = 0
while True:
    n1 = int(input('Digite um valor:'))
    n3 = ' '
    while n3 not in 'PpIi':
        n3 = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    soma = n2 + n1
    if n3 == 'P' and (soma % 2) == 0:
        print(f'Você escolheu {n1} e o computador {n2}. Total deu {soma} que é Par.')
        print('Você VENCEU!')
        cont += 1
        print('Vamos jogar novamente...')
    elif n3 == 'P' and (soma % 2) != 0:
        print(f'Você escolheu {n1} e o computador {n2}. Total deu {soma} que é Ímpar.')
        print('Você PERDEU!')
        break
    elif n3 == 'I' and (soma % 2) != 0:
        print(f'Você escolheu {n1} e o computador {n2}. Total deu {soma} que é Ímpar.')
        print('Você VENCEU!')
        cont += 1
        print('Vamos jogar novamente...')
    else:
        print(f'Você escolheu {n1} e o computador {n2}. Total deu {soma} que é Par.')
        print('Você PERDEU!')
        break
print('-=-'*20)
print(f'GAME OVER! Você venceu {cont} vezes.')







