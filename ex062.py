# na variavel "mais" colococamos = 10 pq 10 é quantidade inicial de termos que mostra, depois conforme o usuário pede ele vai mostar mais  somando a variaável "mais" com a variável "total"
pa = int(input('Qual o primeiro termo da PA?'))
razao = int(input('Qual a razão da PA?'))
termo = pa
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Prograssão finalizada com {} termos mostrados.'.format(total))






