'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas
-O nome com todas as letras minúsculas
-Quantas letras há ao todo (sem considerar espaços)
-Quantas letras tem o primeiro nome
'''

print('Analizando seu nome...')
print('Caixa alta: ', nome.upper())
print('Caixa baixa: ', nome.lower())

aux1 = nome.split()
aux2 = ''.join(aux1)
totLetras = len(aux2)

print('"{}" contém {} letras'.format(nome, totLetras))

print('"{}" contém {} letras'.format(aux1[0], len(aux1[0])))
