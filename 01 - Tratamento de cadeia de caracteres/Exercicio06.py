'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Exemplo:
Nome: "Ana Maria de Souza"
Primeiro nome: "Ana"
Último nome: "Souza"
'''

name = str(input('Digite seu nome completo: ')).strip().title()
print('Analisando nome... Aguarde')
nameList = name.split()
print('Primeiro nome: {}'.format(nameList[0]))
print('Último nome: {}'.format(nameList[len(nameList)-1]))
