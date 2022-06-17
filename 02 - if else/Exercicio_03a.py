'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas
'''


d = int(input('Digite a distância da viagem (km): '))

if d <= 200:
    print('Total a pagar: R${:.2f}'.format(d * 0.5))
elif d > 200:
    print('Total a pagar: R${:.2f}'.format(d * 0.45))
else:
    print('Você digitou a distância correta?')
