

def leiaInt(num):
    while True:
        perg = str(input('Digite um número: '))
        if perg.isnumeric():
            print(f' Você acabou de digitar o número {perg}')
            break
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')


# Programa principal
perg = leiaInt('Digite um número: ')
