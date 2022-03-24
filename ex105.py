dicio = dict()



def notas(* notas, sit = False):
    """
    --> Essa função recebe as notas dos alunos e retorna um dicionário com
    as informações: quantidade de notas (total), a maior nota, a menor nota,
    a média da turma e a situação (opcional).
    :param notas: valor das notas
    :param sit: situação
    :return:
    """
    cont = maior = menor = 0
    for valor in notas:
        cont += 1
        if cont == 1 or valor > maior:
            maior = valor
            dicio['maior'] = maior
        if cont == 1 or valor < menor:
            menor = valor
            dicio['menor'] = menor
    dicio[f'total'] = cont
    média = sum(notas) / cont
    dicio[f'média'] = média
    if sit:
        if média >= 7:
            dicio['situação:'] = 'Boa'
        elif 6 <= média < 7:
            dicio['situação:'] = 'Razoável'
        else:
            dicio['situação:'] = 'Ruim'


# Programa Principal
# resp = notas(5.5, 4.5, 10, 6.5, sit=True)
# print(dicio)
help(notas)
