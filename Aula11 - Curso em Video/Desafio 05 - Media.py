'''
Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
* Média < 5,0 == REPROVADO;
* Média > 5,0 && Média < 6,9 == RECUPERAÇÃO;
* Média > 7,0 == APROVADO;
'''
'''Observações:
1 - Optei por não utilizar a biblioteca statiscis
2 - Lógica contruída de forma a facilitar a inclusão de mais notas
3 - Lógica contruída de forma a facilitar a modificação para o usuário informar o número de notas'''

def valida_nota(pergunta):
  while True:
    try:
      nota = float(input(pergunta))
      if nota < 0:
        print('Digite um valor entre 0 e 10')
        continue
      elif nota > 10:
        print('Digite um valor entre 0 e 10')
        continue
      else:
        break
    except ValueError:
      print('Valor inválido, digite um valor entre 0 e 10')
      continue
    except:
      print('Oops! Algo errado aconteceu...')
  return nota

nota = []
for i in range(1,3):
  n =valida_nota(f"Digite a {i}° nota: ") 
  nota.append(n)
media = sum(nota)/len(nota)
if media < 5:
  print(f'média: {media} - REPROVADO')
elif 7 > media >= 5:
  print(f'média: {media} - RECUPERAÇÃO')
else:
  print(f'média: {media} - APROVADO')
