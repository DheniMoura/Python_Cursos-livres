'''
Faça um program aque leia o nome de nascimento de um jovem e informe, de acordo com a sua idade:
* Se ele ainda vai se alistar ao serviço militar;
* Se é a hora de se alistar;
* Se já passou do tempo do alistamento;
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
(Utilizar dados do sistema)
'''

from datetime import date

def valida_ano_nasc(pergunta):
  atual = date.today().year
  while True:
    try:
      ano = int(input(pergunta))

      if ano > atual:
        print('Ano de nascimento inválido, digite novamente')
        continue
      else:
        break
    except ValueError:
      print('Número inválido, digite novamente...')
      continue
    except:
      print('Oops, algo errado aconteceu...')
  return ano

atual = date.today().year
nome = str(input('Digite seu nome: '))
nasc = valida_ano_nasc('Digite seu ano de nascimento: ')
idade = atual - nasc
print(f'Quem nasceu em {nasc} completa {idade} anos em {atual}')

if idade == 18:
  prit("Você precisa se alistar IMEDIATAMENTE!")
elif idade < 18:
  saldo = 18 - idade
  ano_alist =  nasc + 18
  if saldo == 1:
    print(f'Ainda falta {saldo} ano')
  else:
    print(f'Ainda faltam {saldo} anos')
  print(f'Seu alistamento será em {ano_alist}')
else:
  saldo = idade - 18
  ano_alist = nasc + 18
  if saldo == 1:
    print(f"Você deveria ter se alistado {saldo} ano atrás")
  else:
    print(f"Você deveria ter se alistado {saldo} anos atrás")
  print(f'Seu alistamento foi em {ano_alist}')
