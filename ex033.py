num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
num3 = float(input('Digite outro número'))
#verificando quem é o menor
menor = num1
if num2 <num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
#verificando quem é o maior
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
