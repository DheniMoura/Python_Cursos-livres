v = float(input('Digite a velocidade do veículo (km/h): '))

if v > 80:
    print('Emitindo multa...')
    print('Valor a pagar: R${:.2f}'.format((v - 80) * 7))
else:
    print('Dirija com cuidado')