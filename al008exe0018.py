from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O seno, cosseno e a tangente de {} é respectivamente {:.3f}, {:.3f}, {:.3f}'.format(ang, seno, coss, tang))
