num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro e ultimo numero: '))
maior = num1
menor = num1

if (num2>maior):
    maior = num2
if num3>maior:
    maior = num3
print('O maior numero é {}'.format(maior))

if (num2<menor):
    menor = num2
if num3<menor:
    menor = num3
print('O menor numero é {}'.format(menor))
