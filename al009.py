frase = 'João Victor Ribeiro Costa'
print(frase[5])
print(frase[5:11])
print(frase[5:11:2])
print(frase[:11])
print(frase[12:])
print(frase[4::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 12))
print(frase.find('Cos'))
print(frase.find('ana'))
print('João' in frase)
print('ana' in frase)
print(frase.replace('João', 'Rapha'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase))
