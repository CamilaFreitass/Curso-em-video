dicio = {}
lista = []
lista2 = list()
while True:
    lista.clear()
    dicio.clear()
    nome = str(input('Nome do Jogador:'))
    dicio['nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou?'))
    for c in range(0, partidas):
        lista.append(int(input(f' Quantos gols na partida {c+1}? ')))
    total = sum(lista)
    dicio['gols'] = lista[:]
    dicio['total'] = total
    lista2.append(dicio.copy())
    perg = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if perg == 'N':
        break
print('-=' * 40)
print(f'{"cod":<4}{"NOME":<30}{"Gols":}{"Total":>30}')
print('--' * 40)
for i, v in enumerate(lista2):
    print(f'{i:<4}{v["nome"]:<30}{v["gols"]}{v["total"]:>30}')
print('-=' * 40)

while True:
    perg = int(input('Mostrar dados de qual jogador? (999 interrompe)'))
    if perg == 999:
        break
    if perg > len(lista2):
        print(f'Não existe jogador número {perg}!')
    else:
        print(f' DADOS DO JOGADOR: {lista2[perg]["nome"]}')
        for i, g in enumerate(lista2[perg]['gols']):
            print(f' Na partida {i+1} fez {g} gols.')
print(f'<<< FIM! >>>')






