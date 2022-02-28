n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
n3 = 0
while n3 != 5:
    print('''       [1] SOMAR
       [2] MULTIPLICAR
       [3] MAIOR
       [4] NOVOS NÚMEROS
       [5] SAIR DO PROGRAMA''')
    n3 = int(input('Qual a opção desejada?'))
    if n3 == 1:
       soma = n1 + n2
       print('A opção desejada foi SOMAR! A soma entre os dois valores digitados é {}'.format(soma))
    elif n3 == 2:
       multiplicaçao = n1 * n2
       print('A opção desejada foi MULTIPLICAR! A multiplicação entre os dois valores é {}'.format(multiplicaçao))
    elif n3 == 3:
       if n1 > n2:
              print('A opção desejada foi MAIOR! O maior valor entre os valores digitados é {}'.format(n1))
       else:
              print('A opção desejada foi MAIOR! O maior valor entre os valores digitados é {}'.format(n2))
    elif n3 == 4:
       print('A opção desejada foi NOVOS NÚMEROS!')
       n1 = int(input('Digite o primeiro valor:'))
       n2 = int(input('Digite o segundo Valor:'))
    elif n3 == 5:
       print('Finalizando...')
    else:
       print('Opção inválida. Tente Novamente')
       print('=-=' * 10)
print('Fim do programa! Volte Sempre!')



