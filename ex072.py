numeros = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
# recebendo o valor
    pergunta = int(input('Escreva um número entre 0 e 20:'))

# validando a integridade do numero
    if pergunta >= 0 and pergunta <= 20:
        print('numero ok')
    else:
        pergunta = int(input('Tente novamente. Escreva um número entre 0 e 20:'))

# traducao do numero
    for posicao in range(0, len(numeros)):
        if posicao == pergunta:
            print(f'O número que você escreveu foi {numeros[posicao]}')

# perguntar se ele vai continuar
    conti = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while conti not in 'SN':
        conti = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if conti == 'S':
        pergunta
    elif conti == 'N':
        break

# finalizando
print('Fim!')















