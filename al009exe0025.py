nome = input('Qual é o seu nome? ')
print('Você tem Silva, no nome: ', 'Silva' in nome)

#resolução exercicio
name = str(input('Digite seu nome completo: ')).strip()
print('Você tem Silva no nome? {}'.format('SILVA' in name.upper()))
