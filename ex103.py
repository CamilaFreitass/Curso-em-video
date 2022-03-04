def ficha(nome, gols):
    if nome == '':
        nome = 'desconhecido'
    if gols == '':
        gols = 0
    return f'O Jogador {nome} fez {gols} gols(s) no campeonato'


# Programa Principal
jogador = str(input('Nome do Jogador: '))
bolas = input('Número de gols: ')
print(ficha(jogador, bolas))


