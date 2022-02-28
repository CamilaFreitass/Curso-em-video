
# expressao = input('Digite a expressão:')
# a = expressao.count('(')
# b = expressao.count(')')
# c = expressao.index('(')
# d = expressao.index(')')
# if a != b or c > d:
#     print('Sua expressão está errada!')
# else:
#     print('Sua expressão está correta!')



expressao = input('Digite a expressão:')
lista_parenteses = [x for x in expressao if x in ['(', ')']]
expressaox = ''.join(lista_parenteses)
pa = expressaox.count('(')
for x in range(pa):
    expressaox = expressaox.replace('()', '')

if expressaox == '':
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
