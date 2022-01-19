#numero de pessoas que embarcou.
embarc = int(input('Quantas das 100 pessoas embarcou? '))
#Formula pra calcular o dinheiro arrecadado.
dinArrec = embarc*1600+40000
print('O dinheiro arrecadado é de {}R$ caso {} pessoas embarquem!'.format(dinArrec, embarc))

#numero de pessoas que embarcou.
embarc = int(input('Quantas das 100 pessoas embarcou? '))
#numero de pessoas que não embarcou.
nao_embarc = int(input('Quantas das 100 pessoas não embarcaram? '))
#Formula pra calcular o dinheiro arrecadado.
dinArrec = embarc*2000+(nao_embarc*400)
print('O dinheiro arrecadado é de {}R$ caso {} pessoas embarquem!'.format(dinArrec, embarc))
