print('Banco Dev')
saque = int(input('Que valor você quer sacar?'))
total = saque
cedula_var = 50
contc = 0

while True:
    if total >= cedula_var:
        total -= cedula_var
        contc += 1
    else:
        # passo 1
        # quando for trocar da cédula de 50 para outra cédula, tem que finalizar e printar o resultado.
        if contc > 0:
            print(f'Total de {contc} cédulas de R${cedula_var}')

        #passo 2
        #zerando o contador
        contc = 0
        
        #passo 2
        # troca de cedula
        if cedula_var == 50:
            cedula_var = 20
        elif cedula_var == 20:
            cedula_var = 10
        elif cedula_var == 10:
            cedula_var = 1

        # passo 3
        if total == 0:
            break

print('Fim!')









