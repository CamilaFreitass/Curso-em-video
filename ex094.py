dicio = {}
lista = []
cont = 0
mulheres = []
idades = []
acima_da_media = []
while True:
    nome = str(input('Nome:'))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Idade:'))
    idades.append(idade)
    cont += 1
    dicio['nome'] = nome
    dicio['sexo'] = sexo
    dicio['idade'] = idade
    lista.append(dicio.copy())
    perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if perg == 'N':
        break
média_idade = ((sum(idades)) / cont)
print(lista)
print(f'O grupo tem {cont} pessoas')
print(f'As mulheres cadastradas foram: {mulheres}')
print('As pessoas com idade acima da média são: ')
for p in lista:
    if p['idade'] >= média_idade:
        print('      ', end='')
        for k, v in p.items():
            print(f' {k} = {v}; ', end='')
        print()

