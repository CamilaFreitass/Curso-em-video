lista = []
dados = []
maispesados = []
maisleves = []
cont = 0
maior = 0
menor = 10000
while True:
    n = dados.append(str(input('Nome:')))
    n1 = dados.append(int(input('Peso:')))
    lista.append(dados[:])
    cont += 1
    dados.clear()
    n2 = ' '
    while n2 not in 'SN':
        n2 = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if n2 == 'N':
        break
nome = []
listadenomes = []
for c in lista:
    if c[1] > maior:
        maior = c[1]
        nome = c[0]
        maispesados.clear()
        listadenomes.clear()
        listadenomes.append(nome)
        maispesados.append(maior)
    elif c[1] == maior:
        maior = c[1]
        nome = c[0]
        listadenomes.append(nome)
        maispesados.append(maior)
nomel = []
listanomesl = []
for h in lista:
    if h[1] < menor:
        menor = h[1]
        nomel = h[0]
        maisleves.clear()
        listanomesl.clear()
        listanomesl.append(nomel)
        maisleves.append(menor)
    elif h[1] == menor:
        menor = h[1]
        nomel = h[0]
        listanomesl.append(nomel)
        maisleves.append(menor)
print('=-'*30)
print(f'As pessoas mais leves foram{listanomesl} com peso {maisleves[0]}')
print('=-'*30)
print(f'As pessoas mais pesadas foram {listadenomes} com o peso {maispesados[0]}')
print('=-'*30)
print(lista)
print('=-'*30)
print(f'Foram cadastradas {cont} pessoas!')




