'''frase = input('Digite uma frase: ')
print(frase.count('A'))
print(frase.find('A'))
print(frase.rfind('A'))'''

#exercicio resolução0
'''frs = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na fras.'.format(frs.lower().count('a')))
print('A primeira letra A aparece na posição {}.'.format(frs.lower().find('a')))
print('A última letra A aparece na posição {}.'.format(frs.lower().rfind('a')))'''

#exercicio resolução1
frs = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na fras.'.format(frs.count('A')))
print('A primeira letra A aparece na posição {}.'.format(frs.find('A')+1))
print('A última letra A aparece na posição {}.'.format(frs.rfind('A')+1))
