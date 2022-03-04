import datetime


def voto():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    anodenasc = int(input('Em que ano você nasceu?'))
    idade = date.year - anodenasc
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade >= 16 and idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif idade >= 18 and idade <= 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade > 70:
        print(f'Com {idade} anos: VOTO OPCIONAL.')


voto()
voto()

