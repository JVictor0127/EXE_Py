velocidade = float(input('Qual a velocidade que o seu carro está percorrendo? '))
maxima = 80
multa = (velocidade-80) * 7
if velocidade > maxima:
    print('Você foi multado, maxima permitidade {}Km/h multa de {}R$'.format(maxima ,multa))
else:
    print('Você esta dirigindo numa boa velocidade, continue assim!!')
