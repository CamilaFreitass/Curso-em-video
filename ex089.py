lista = []
dados = []
while True:
    nome = dados.append(str(input('Nome:')))
    nota1 = dados.append(float(input('Nota 1:')))
    nota2 = dados.append(float(input('Nota 2:')))
    media = (sum(dados[1:])) / 2
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg == 'N':
        break
print('-'*30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, l in enumerate (lista):
    print(f'{i:<4}{l[0]:<10}{l[3]:>8.1f}')
pergt = ' '
while pergt != 999:
    pergt = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if pergt == 999:
        break
    print(f'Notas de {lista[pergt][0]} são {lista[pergt][1:3]}')
print('Fim!')










