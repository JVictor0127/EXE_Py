nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua media é: {}'.format(media))
if media >= 6:
    print('Sua nota esta boa, parabens!!!')
else:
    print('Sua nota não está tão boa, vamos melhorar')
