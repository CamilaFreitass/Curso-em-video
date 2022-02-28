dicio = {}
nome = str(input('Nome do Jogador:'))
dicio['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou?'))
lista = []
#pergunta quantos gols o jogador fez em cada partida
for c in range(0, partidas):
#adiciona os gols a lista
    lista.append(int(input(f' Quantos gols na partida {c}? ')))
total = sum(lista)
#adiciona a lista de gols ao dicionário
dicio['gols'] = lista
#adiciona o total de gols ao dicionário
dicio['total'] = total
print('-=' * 40)
#mostra o que tem dentro do dicionário
print(dicio)
print('-=' * 40)
#mostra as chaves e seus valores correspondentes
for k,  v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
#mostra o nome do jogador e quantas partidas ele jogou
print(f'O jogador {nome} jogou {partidas} partidas.')
#mostra quantos gols o jogador fez em cada partida
for c in range(0, len(lista)):
    print(f'=> Na partida {c}, fez {lista[c]} gols.')
#mostra o total de gols
print(f'Foi um total de {total} gols.')
