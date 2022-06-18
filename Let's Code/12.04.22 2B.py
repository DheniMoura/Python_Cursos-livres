'''Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘ | ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. '''

def validacao_inteiro_positivo(pergunta): # Validação de número inteiro positivo entre 1 e 20
  while True:
    try:
      x = int(input(pergunta))
      if x >= 1 and x <= 20:
        break
    except ValueError:
      print('Oops! Número inválido. Tente novamente...')
      continue
    except:
      print('Oops! Algo errado aconteceu...')
    if x < 0 or x > 20:
      print('O valor precisa ser inteiro entre 1 e 20')
    continue
  return x

def retangulo(): # Funçao retângulo
  tamanho_linha = validacao_inteiro_positivo("Digite o número de linhas: ")
  tamanho_coluna = validacao_inteiro_positivo("Digite o número de colunas: ")

  meio = " "
  linha = "-"
  print(f"+{linha*tamanho_linha}+")
  for i in range(0,tamanho_coluna):
    print(f"|{meio*tamanho_linha}|")
  print(f"+{linha*tamanho_linha}+")

retangulo()
