'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random
from time import sleep

print('*' * 40)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('Digite 6 para sair')
print('*' *40)

while True:
    pc = random.randint(0,5) #Gera um número aleatório
    vc = int(input('Qual seu palpite? '))
    print('Processando...')
    sleep(1) #faz uma pequena pausa(definida), neste caso para parecer que o PC tá processando
    if pc == vc:
        print('Eu pensei no número {}, você venceu!'.format(pc))
    elif vc == 6:
        print('Encerrando..')
        break
    else:
        print('Eu pensei no número {}, você não acertou!'.format(pc))
