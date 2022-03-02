from time import sleep

def maior(* numeros):
    cont = maior = 0
    for i, v in enumerate(numeros):
        if cont == 0:
            maior = v
        elif v > maior:
            maior = v
        print(f' {v} ', end='')
        sleep(0.5)
        cont +=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior} ')



# Programa Principal
maior(9, 7, 12, 2, 6, 1, 3)
maior(8, 22, 31, 14, 5, 0)
maior(10, 1, 65)
maior(3)
maior()
