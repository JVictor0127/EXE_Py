'''nome = input('Digite seu nome completo: ')
lista_nome0 = (nome.split())
print('Primeiro nome: ', lista_nome0[0])
lista_nome_fim = lista_nome0.pop()
print('Último nome: ', lista_nome_fim)'''

#exercicio resolução
n = str(input('Digite seu nome: ')).strip()
l_name = n.split()
print('Seu primeiro nome é: {}'.format(l_name[0]))
print('Seu último nome é: {}'.format(l_name[-1]))
