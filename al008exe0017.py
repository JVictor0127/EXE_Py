from math import pow, sqrt, hypot

'''catop = float(input('Digite o cateto oposto: '))
catad = float(input('Digite o cateto adjacente '))
hip = sqrt(pow(catop, 2) + pow(catad, 2))
print('Com o cateto oposto valendo {} e o adjacente {} a hipotenusa vale {:.3f}'.format(catop, catad, hip))'''
catop = float(input('Digite o cateto oposto: '))
catad = float(input('Digite o cateto adjacente '))
hip = hypot(catop, catad)
print('Com o cateto oposto valendo {} e o adjacente {} a hipotenusa vale {:.2f}'.format(catop, catad, hip))
