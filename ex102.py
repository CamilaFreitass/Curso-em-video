def fatorial(num, show=False):
    """
    - Função para calcular o fatorial de um número.
    :param num: O número que deseja saber o fatorial.
    :param show: parametro opcional para mostrar ou não o cálculo.
    :return: retorna o fatorial
    """
    f = 1
    for c in range (num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#print(fatorial(5, show=False))
help(fatorial)

