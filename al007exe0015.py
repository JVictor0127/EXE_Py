dias = int(input('Quantos dias que o carro foia lugado? '))
km = float(input('Quantos km foram percorridos? '))
print('Como você alugou o carro por {} dias e percorreu {}km, o preço a ser pago é de {} \nLevando em consideração que o aluguel por dia custa 60.00R$ e é cobrado uma taxa de 0.15R$'.format(dias, km, dias*60+km*0.15))
