'''
Faça um programa que leia uma frase pelo teclado e mostre:<br>
* Quantas vezes aparece a letra "A";
* Em que posição ela aparece pela primeira vez;
* Em que posição ela aparece pela última vez.
'''

frase = str(input('Digite sua frase favorita: ')).strip().upper()
print('Analisando frase... ')
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('Primeira posição com letra "A": {}'.format(frase.find('A')+1))
print('Última posição com letra "A": {}'.format(frase.rfind('A')+1))
