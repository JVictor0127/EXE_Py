ano = int(input('Digite um ano qualquer: '))
biss = (ano % 4)

if biss == 0:
    biss2 = biss % 100
    if biss2 != 0:
        print('O ano {} é bissexto!'.format(ano))
    else:
        biss3 = biss % 400
        if biss != 0:
            print('O ano {} não é bissexto!'.format(ano))
        else:
            print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
