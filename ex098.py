from time import sleep

def contador():
    print('-=' * 30)
    print('Contagem de 1 até 10 de 1 em 1:')
    cont = list(range(0, 10))
    for c in cont:
        print(f' {c+1} ', end='')
        sleep(1)
    print('FIM!')
    print('-=' * 30)
    print('Contagem de 10 até 0 de 2 em 2:')
    lista = list(range(10, -2, -2))
    for g, v in enumerate(lista):
        print(f' {v} ', end='')
        sleep(1)
    print('FIM!')
    print('-=' * 30)
    print('Agora é a sua vez de personalizar a contagem!')
    ini = int(input('Início: '))
    fim = int(input('Fim: '))
    pas = int(input('Passo: '))
    print(f'Contagem de {ini} até {fim} de {pas} em {pas} ')
    if pas == 0:
        pas = 1
    if ini > fim:
        if pas < 0:
            pas = pas * (-1)
        if fim < 0:
            fim = fim - 1
        if fim > 0:
            fim = fim - 1
        lista2 = list(range(ini, fim, -pas))
    elif fim > ini:
        if pas < 0:
            pas = pas * (-1)
        if fim < 0:
            fim = fim - 1
        if fim > 0:
            fim = fim + 1
        lista2 = list(range(ini, fim, pas))
    print('-=' * 30)
    sleep(1)
    for h, f in enumerate(lista2):
         print(f' {f} ', end='')
         sleep(1)
    print('FIM!')


contador()
