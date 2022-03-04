def leiaInt(msg):
    #essa variável ok é justamente para verificar se ocorreu conforme o esperado
    #enquanto ela estiver como False está sinalizando que tem algo de errado
    # quando ela passar para True está sinalizando que ocorreu tudo dentro do esperado
    ok = False
    valor = 0
    while True:
        #"isnumeric() é um método embutido usado para manipulação de strings.
        # O método isnumeric() retorna "True" se todos os caracteres da string foram numéricos,
        # caso contrário, retorna "False"
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

