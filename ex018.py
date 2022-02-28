import math
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo {:.2f} tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(ângulo, seno, cosseno, tangente))
