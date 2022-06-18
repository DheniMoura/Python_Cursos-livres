'''
Para um número *n* informado pelo usuário, use uma função
que receba um valor *n* inteiro e imprima até a n-ésima linha
1
1 2
1 2 3 
...... 
1 2 3 ... n '''

n = int(input('Digite um número: '))
a = 0
for i in range(1,n+1):
  for j in range(1,i+1):
    a += 1
    print(f'{a} ', end='')
  print('')
  a = 0
