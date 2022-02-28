a = float(input('Qual o tamanho da primeira reta?'))
b = float(input('Qual o tamanho da segunda reta?'))
c = float(input('Qual o tamanho da terceira reta?'))
if (a+b)>c and (b+c)>a and (c+a)>b:
    print('Forma triângulo!')
    if a == b == c:
        print('Triângulo Equilátero')
    elif a == b or b == c or c == a:
        print('Triângulo Isósceles!')
    else:
        print('Triângulo Escaleno!')
else:
    print('Não forma triângulo!')
