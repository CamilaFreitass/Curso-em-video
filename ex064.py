# Fiz tudo isso sozinha! Eu sou foda!
n1 = int(input('Digite um número [999 para parar]:'))
cont = 0
soma = n1
while n1 != 999:
    n1 = int(input('Digite um número [999 para parar]:'))
    cont = cont + 1
    if n1 != 999:
        soma = soma + n1
print(f'Você digitou {cont} números e a soma entre eles é {soma}')












