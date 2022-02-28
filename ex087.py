valorespares = []
terceiracoluna = []
segundalinha = []
n1 = int(input('Digite um valor para [0, 0]:'))
if (n1 % 2) == 0:
    valorespares.append(n1)
n2 = int(input('Digite um valor para [0, 1]:'))
if (n2 % 2) == 0:
    valorespares.append(n2)
n3 = int(input('Digite um valor para [0, 2]:'))
if (n3 % 2) == 0:
    valorespares.append(n3)
terceiracoluna.append(n3)
n4 = int(input('Digite um valor para [1, 0]:'))
if (n4 % 2) == 0:
    valorespares.append(n4)
segundalinha.append(n4)
n5 = int(input('Digite um valor para [1, 1]:'))
if (n5 % 2) == 0:
    valorespares.append(n5)
segundalinha.append(n5)
n6 = int(input('Digite um valor para [1, 2]:'))
if (n6 % 2) == 0:
    valorespares.append(n6)
segundalinha.append(n6)
terceiracoluna.append(n6)
n7 = int(input('Digite um valor para [2, 0]:'))
if (n7 % 2) == 0:
    valorespares.append(n7)
n8 = int(input('Digite um valor para [2, 1]:'))
if (n8 % 2) == 0:
    valorespares.append(n8)
n9 = int(input('Digite um valor para [2, 2]:'))
if (n9 % 2) == 0:
    valorespares.append(n9)
terceiracoluna.append(n9)
print('-='*30)
print(f'[ {n1} ][ {n2} ][ {n3} ]')
print(f'[ {n4} ][ {n5} ][ {n6} ]')
print(f'[ {n7} ][ {n8} ][ {n9} ]')
print('-='*30)
print(f'A soma dos valores pares é {sum(valorespares)}')
print(f'A soma dos valores da terceira coluna é {sum(terceiracoluna)}')
print(f'O maior valor da segunda linha foi {max(segundalinha)}')
