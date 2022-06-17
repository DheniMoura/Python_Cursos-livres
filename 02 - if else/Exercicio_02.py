'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A  multa vai custar R$7 por cada Km acima do limite.
'''

v = float(input('Digite a velocidade do veículo (km/h): '))

if v > 80:
    print('Emitindo multa...')
    print('Valor a pagar: R${:.2f}'.format((v - 80) * 7))
else:
    print('Dirija com cuidado')