'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem, e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.(?)'''


def somaImposto(taxaImposto, custo):
    c = custo
    t = taxaImposto / 100
    m = c * (1 + t)
    return f'{m:.2f}'


taxa = float(input('Taxa de imposto sobre vendas (em porcentagem): '))
custo = float(input('Custo do item (em reais): '))
print(f'Custo após imposto R${somaImposto(taxa, custo)}')
