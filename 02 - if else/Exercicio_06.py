'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento:
Para salários superiores a R$1.250,00, calcule um aumento de 10%;
Para salários inferiores ou iguais, o aumento é de 15%.'''

from time import sleep
sal = float(input('Salário: R$'))
print('Calculando aumento...')
sleep(1)

aumento = sal * 1.15 if sal <= 1250 else sal * 1.1
print('Salário corrigido: R${:.2f}'.format(aumento))