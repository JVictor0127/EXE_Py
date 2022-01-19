from random import choice
al1 = str(input('Digite o nome do aluno: '))
al2 = str(input('Digite o nome do aluno: '))
al3 = str(input('Digite o nome do aluno: '))
al4 = str(input('Digite o nome do aluno: '))
lista = [al1, al2, al3, al4]
sort = choice(lista)
print('O aluno sorteado foi: {}'.format(sort))
