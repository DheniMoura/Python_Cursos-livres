d = int(input('Digite a distância da viagem (km): '))

if d <= 200:
    print('Total a pagar: R${:.2f}'.format(d * 0.5))
elif d > 200:
    print('Total a pagar: R${:.2f}'.format(d * 0.45))
else:
    print('Você digitou a distância correta?')
