#Crie um programa que faça o computador jogar jokenpô com você
from random import randint

def validacao_jokenpo(pergunta):
  while True:
    try:
      x = int(input(pergunta))
      if 1 <= x <= 3:
        break
    except ValueError:
      print('Oops! Número inválido. Tente novamente...')
      continue
    except:
      print('Oops! Algo errado aconteceu...')
    if int(x) < 0:
      print('O número precisa ser inteiro e positivo')
    continue
  return x

def menu():
  print("Escolha sua jogada!")
  print("1 - PEDRA")
  print("2 - PAPEL")
  print("3 - TESOURA")

def jogada(num):
  if num == 1:
    print("Você jogou PEDRA")
  elif num == 2:
    print("Você jogou PAPEL")
  elif num == 3:
    print("Você jogou TESOURA")

print("***JOKENPÔ***")
menu()

pessoa = validacao_jokenpo("Sua vez! ")
jogada(pessoa)

maquina = randint(1,3)

#construir a condição de comparação das jogadas e apresentar o resultado
#FAZER O JOGO CONTÍNUO ATÉ A PESSOA DECIDIR SAIR