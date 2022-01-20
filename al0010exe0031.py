distancia = float(input('Qual a distancia da viagem em km? '))
passagem_menor = (distancia * 0.50)
passagem_maior = (distancia * 0.45)

if distancia <= 200:
    print('O preço da passagem é {}'.format(passagem_menor))
else:
    print('O preço da passagem custa {}'.format(passagem_maior))
