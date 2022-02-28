a = float(input('Qual o tamanho da primeira reta?'))
b = float(input('Qual o tamanho da segunda reta?'))
c = float(input('Qual o tamanho da terceira reta?'))
print('Forma um triângulo!' if (a+b)> c and (b+c)>a and (a+c)>b else 'Não forma uma triângulo!')

