#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando nome... ')
print('O nome contém "Silva": {}'.format('SILVA' in nome.upper()))
