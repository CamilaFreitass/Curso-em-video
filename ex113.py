global perg, pergt

def leiaInt(num):
    while True:
        try:
            perg = int(input('Digite um número Inteiro: '))
        except ValueError:
            print(f'\033[0;31m Erro: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    return perg


def leiaReal(num):
    while True:
        try:
            pergt = float(input('Digite um número Real: '))
        except ValueError:
            print(f'\033[0;31m Erro: por favor, digite um número real válido.\033[m')
        else:
            break
    return pergt



# Programa principal
perg = leiaInt('Digite um número inteiro: ')
pergt = leiaReal('Digite um número real: ')
print(f'O número inteiro digitado foi {perg} e o real foi {pergt}')
