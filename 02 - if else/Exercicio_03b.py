d = int(input('Digite a distância da viagem (km): '))
p = d * 0.5 if d <= 200 else d * 0.45
print('Total a pagar: R${:.2f}'.format(p))