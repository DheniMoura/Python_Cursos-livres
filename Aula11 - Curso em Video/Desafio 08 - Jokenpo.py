#Crie um programa que faça o computador jogar jokenpô com você
from random import randint

def validacao_jokenpo(pergunta):
  while True:
    try:
      x = int(input(pergunta))
      if 0 <= x <= 3:
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
  print("0 - ENCERRAR O JOGO")

def jogada(num):
  if num == 1:
    print("Você jogou PEDRA")
  elif num == 2:
    print("Você jogou PAPEL")
  elif num == 3:
    print("Você jogou TESOURA")
  elif num == 0:
    print("Encerrando...")

print("***JOKENPÔ***")

while True:
  menu()

  pessoa = validacao_jokenpo("Sua vez! ")
  print(pessoa)
  jogada(pessoa)
  if pessoa == 0:
    break
  #maquina = randint(1,3)

#construir a condição de comparação das jogadas e apresentar o resultado
# 1- FAZER O JOGO CONTÍNUO ATÉ A PESSOA DECIDIR SAIR; OU
# 2- FAZER "MELHOR DE TRÊS" OU "MELHOR DE CINCO", CONFORME O JOGADOR ESCOLHER