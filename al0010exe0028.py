import random

computador = random.randint(0, 5)
pessoa = int(input('Adivinhe qual o numero que o coputador escolheu: '))
if pessoa == computador:
    print('Parebens o computador escolheu {}, assim como você que escolheu {}!!'.format(computador, pessoa))
else:
    print('Infelismente o computador escolheu o numero {}, e você o numero {}, tente novamente.'.format(computador, pessoa))
