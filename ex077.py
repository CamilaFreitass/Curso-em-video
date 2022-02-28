palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for posicao in palavras:
    print(f'\nNa palavra {posicao.upper()} temos', end=' ')
    for vogal in posicao:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')

