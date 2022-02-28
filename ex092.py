dicio = {}
dicio['Nome'] = str(input('Nome: '))
anodenasc = int(input('Ano de Nascimento: '))
dicio['idade'] = (2022 - anodenasc)
ctps = int(input('Carteira de Trabalho (0 não tem): '))
dicio['ctps'] = ctps
if ctps != 0:
    dicio['Ano de contratação:'] = int(input('Ano de contratação: '))
    dicio['Salário'] = float(input('Salário: '))
    aposent = (((dicio['Ano de contratação:']) + 35) - anodenasc)
    dicio['aposentadoria'] = aposent
print(dicio)
for k, v in dicio.items():
    print(f'{k} tem o valor {v}')
