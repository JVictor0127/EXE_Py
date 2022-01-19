cidade = str(input('Digite o nome de uma cidade: '))
cidade_name = cidade.split()
print('Tem a palavra Santo nesta Cidade: {}'.format('Santo' in cidade_name[0]))

#resolução do execicio
cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade_name = cidade.split()
print('Tem a palavra Santo nesta Cidade: {}'.format(cidade_name[0].upper() == 'SANTO'))
