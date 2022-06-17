#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print('Digite o ano que quer analisar. Para analisar o ano atual, digite 0')
ano = int(input('Ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
    