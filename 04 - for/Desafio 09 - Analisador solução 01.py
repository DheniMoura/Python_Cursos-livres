'''
leia o nome, idade e sexo de 4 pessoas. Mostrar:
* média de idade do grupo
* o nome do homem mais velho
* quantas mulheres tem menos de 20 anos'''

# Solução 01

def validacao_idade(pergunta):  # Validação de número inteiro positivo entre 1 e 120
    while True:
        try:
            x = int(input(pergunta))
            if x >= 1 and x <= 120:
                break
        except ValueError:
            print('Oops! Número inválido. Tente novamente...')
            continue
        except:
            print('Oops! Algo errado aconteceu...')
        if x < 0 or x > 120:
            print('O valor precisa ser inteiro entre 1 e 120')
        continue
    return x


soma_idade = 0
mais_velho_nome = ""
mais_velho_idade = 0
menor20 = 0

for i in range(0, 4):
    print(f'---- {i + 1}° Pessoa ----')
    nome = str(input('Nome: '))
    idade = validacao_idade('Idade: ')
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade

    if sexo == 'M' and mais_velho_idade < idade:
        mais_velho_idade = idade
        mais_velho_nome = nome

    if sexo == 'F' and idade < 20:
        menor20 += 1


media = soma_idade / 4
print(f'Média de idade do grupo: {media}')
print(f'O homem mais velho é {mais_velho_nome} com {mais_velho_idade} anos de idade')
if menor20 == 0:
    print('Não há mulheres com menos de 20 anos')
elif menor20 == 1:
    print('Há uma mulher com menos de 20 anos')
else:
    print(f'{menor20} mulheres tem menos de 20 anos de idade')
