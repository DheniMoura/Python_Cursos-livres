'''Escreva um programa que leia dois números inteiro e compare-os, mostrando na tela uma mensagem:
* "O primeiro valor é maior"
* "O segundo valor é maior"
* "Não tem valor maior, os dois valores são iguais" '''

def validacao_inteiro_positivo(pergunta):
  while True:
    try:
      x = int(input(pergunta))
      if x >= 0:
        break
    except ValueError:
      print('Oops! Número inválido. Tente novamente...')
    except:
      print('Oops! Algo errado aconteceu...')
    if int(x) < 0:
      print('O número precisa ser inteiro e positivo')
    continue
  return x

n1 = validacao_inteiro_positivo('Digite o primeiro número: ')
n2 = validacao_inteiro_positivo('Digite o segundo número: ')

if n1 > n2:
  print('o primeiro valor é maior')
elif n2 > n1:
  print('o segundo valor é maior')
else:
  print("Não tem valor maior, os dois valores são iguais")
