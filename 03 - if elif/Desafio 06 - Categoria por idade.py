'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
* até 9 anos: mirim
* até 14 anos: infantil
* até 19 anos: junior
* até 25 anos: sênior
* acima: master'''
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


print("NATAÇÃO - CATEGORIAS POR IDADE")

atual = date.today().year
nasc = valida_ano_nasc("Digite o ano de nascimento: ")
idade = atual - nasc

if idade <= 9:
    print(f"idade: {idade}\nCategoria: mirim")
elif idade <= 14:
    print(f"idade: {idade}\nCategoria: infantil")
elif idade <= 19:
    print(f"idade: {idade}\nCategoria: junior")
elif idade <= 25:
    print(f"idade: {idade}\nCategoria: sênior")
else:
    print(f"idade: {idade}\nCategoria: master")
