nota1 = float(input('Qual a primeira nota?'))
nota2 = float(input('Qual a segunda nota?'))
media = (nota1 + nota2)/2
if media < 5:
    print('\033[1;31mREPROVADO\033[1;31;m')
elif media >= 5.0 and media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[1;33M')
elif media >= 7.0:
    print('\033[1;34mAPROVADO\033[1;34m')
    

