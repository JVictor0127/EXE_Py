nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^25}!'.format(nome))
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma vale {} \n o produto vale {} \n a dvisão vale{:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira vale {}, a potencia vale {}'.format(di, p))
