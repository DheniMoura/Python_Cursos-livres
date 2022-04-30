'''
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.\n
Calcule o valor da prestação mensal, sabendo que ela não pode axceder 30% do salário ou então o empréstimo será negado.
DESCONSIDERAR JUROS
'''

print("SIMULAÇÃO DE EMPRÉSTIMO IMOBILIÁRIO")

c = float(input('Preço do imóvel: R$'))
s = float(input('Salário: R$'))
a = int(input('Prazo para pagamento, em anos: '))

p = c / (a * 12)

print(
    f'Pagando um total de {c:.2f} em {a} anos, o valor da parcela é R${p:.2f}')

if (p / s) <= 0.3:
    print('Empréstimo pré aprovado')
else:
    print("""Emprestímo bloqueado
Parcela excede 30% do salário""")

print(f"Parcela equivalente a {(p/s)*100:.1f}% do salário")
