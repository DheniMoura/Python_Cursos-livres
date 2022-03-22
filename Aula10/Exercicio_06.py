from time import sleep
sal = float(input('Salário: R$'))
print('Calculando aumento...')
sleep(1)

aumento = sal * 1.15 if sal <= 1250 else sal * 1.1
print('Salário corrigido: R${:.2f}'.format(aumento))