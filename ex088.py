import random
print('-'*40)
print('JOGA NA MEGA SENA')
print('-'*40)
n1 = int(input('Quantos jogos você quer que eu sorteie:'))
print(f'-=-=-= SORTEANDO {n1} JOGOS -=-=-=')
for c in range (0, n1):
    lista = [random.randint(1, 60), random.randint(1, 60), random.randint(1, 60),
             random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)]
    lista.sort()
    print(f'O jogo {c+1}: {lista}')
print(f'-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')

