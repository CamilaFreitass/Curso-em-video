# o último "cont" serve para somar até ele chegar no cont igual a "n"
# O primeiro "cont = 3" é a criação da variável, ou seja, ela conta os dois primeiros termos que já definimos
# que são o t1 e t2. Se "n" for menor que 3 a função "while" nem vai entrar em ação.
# Se for igual a 3 a função "while" vai executar o comando uma vez. E assim por diante.
print('Sequência de Fibonacci')

n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' →  {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ... FIM')

