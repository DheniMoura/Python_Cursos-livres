'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

# cada um dos lados precisa menor que a soma dos outros dois lados.
a = float(input('Lado 1 (cm): '))
b = float(input('Lado 2 (cm): '))
c = float(input('Lado 3 (cm): '))

if a + b > c and a + c > b and b + c > a:
    print('Triângulo feito!')
else:
    print('\033[31mNão forma\033[37m um triângulo.')
