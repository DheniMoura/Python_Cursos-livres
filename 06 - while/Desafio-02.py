'''
Melhore o jogo do DESAFIO DE ADIVINHAÇÃO onde o computador vai “pensar” em um número 
entre 0 e 5. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no 
final quantos palpites foram necessários para vencer.
'''

import random

print('*' * 40)
print('Vou pensar em um número entre 0 e 10, tente adivinhar!')
print('*' *40)

pc = random.randint(0,10) #Gera um número aleatório
acertou = False
palpites = 0

while not acertou:    
    vc = int(input('Qual seu palpite? '))
    palpites +=1
    if pc == vc:
        acertou = True
    else:
        if vc < pc:
            print('Mais... tente de novo')
        elif vc > pc:
            print('Menos... tente de novo')
print(f'Acertou com {palpites} tentativas')