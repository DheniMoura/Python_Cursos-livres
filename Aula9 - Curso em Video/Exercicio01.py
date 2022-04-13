nome = str(input('Digite o nome completo: ')).strip()
print('Analizando seu nome...')
print('Caixa alta: ', nome.upper())
print('Caixa baixa: ', nome.lower())

aux1 = nome.split()
aux2 = ''.join(aux1)
totLetras = len(aux2)

print('"{}" contém {} letras'.format(nome, totLetras))

print('"{}" contém {} letras'.format(aux1[0], len(aux1[0])))
