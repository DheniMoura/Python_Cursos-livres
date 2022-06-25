'''
leia o nome, idade e sexo de 4 pessoas. Mostrar:
* média de idade do grupo
* o nome do homem mais velho
* quantas mulheres tem menos de 20 anos'''

# Solução 02 - utilizando lista e dicionário


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


lista = []
for i in range(0, 4):
    nome = str(input(f'Digite o nome da {i + 1} pessoa: '))
    idade = validacao_idade(f'Digite a idade da {i + 1} pessoa: ')
    sexo = str(input(f'Digite o sexo da {i + 1} pessoa (M/F): ')).upper()
    dicio = {'nome': nome, 'idade': idade, 'sexo': sexo}
    lista.append(dicio)

soma_idade = 0
homem_mais_velho = ''
idade_hmv = 0
menores_de_20 = 0

for item in lista:
    soma_idade += item['idade']
    if item['sexo'] in 'Mm' and item['idade'] > idade_hmv:
        homem_mais_velho = item['nome']
        idade_hmv = item['idade']
    if item['sexo'] in 'Ff' and item['idade'] < 20:
        menores_de_20 += 1

media = soma_idade/len(lista)
print(f'Média de idade do grupo: {media}')

print(f'O homem mais velho é {homem_mais_velho} com {idade_hmv} anos de idade')

if menores_de_20 == 0:
    print('Não há mulheres com menos de 20 anos')
elif menores_de_20 == 1:
    print('Há uma mulher com menos de 20 anos')
else:
    print(f'{menores_de_20} mulheres tem menos de 20 anos de idade')
