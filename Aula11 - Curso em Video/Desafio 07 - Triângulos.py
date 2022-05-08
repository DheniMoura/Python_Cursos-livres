'''
Desenvolva um programa que leia o comprimento de três retas e dia ao usuário se elas podem ou não formar um triângulo, diga que o tipo de trângulo que será formado:
* Equilátero (todos os lados iguais)
* Isósceles (dois lados iguais)
* Escaleno (todos os lados diferentes)'''
# cada um dos lados precisa menor que a soma dos outros dois lados.


def validacao_float_positivo(pergunta):
    while True:
        try:
            x = float(input(pergunta))
            if x >= 0:
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


a = validacao_float_positivo('Lado 1 (cm): ')
b = validacao_float_positivo('Lado 2 (cm): ')
c = validacao_float_positivo('Lado 3 (cm): ')

if a + b > c and a + c > b and b + c > a:
    print('Triângulo feito!')
    if a == b == c:
        print("Esse é um TRIÂNGULO EQUILÁTERO")
    elif a != b and b != c and c != a:
        print("Esse é um TRIÂNGULO ESCANELO")
    else:
        print("Esse é um TRIÂNGULO ISÓSCELES")
else:
    print('Não forma um triângulo.')
