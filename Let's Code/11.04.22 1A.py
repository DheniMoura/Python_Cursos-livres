'''
Para um número *n* informado pelo usuário, use uma função
que receba um valor *n* inteiro e imprima até a n-ésima linha
1
2 2
3 3 3 
......
n n ... n '''

n = int(input('Digite um número: '))

for i in range(1, n+1):
  print(f'{i} '* i)
