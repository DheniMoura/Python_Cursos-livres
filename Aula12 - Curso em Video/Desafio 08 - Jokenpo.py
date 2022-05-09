# Crie um programa que faça o computador jogar jokenpô com você
from random import randint
from time import sleep


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
    print("Suas opções: ")
    print("1 - PEDRA")
    print("2 - PAPEL")
    print("3 - TESOURA")
    print("0 - Encerrar o jogo")


def jokenpo(jogada_pessoa, jogada_maquina):
    p = jogada_pessoa
    m = jogada_maquina
    pv = 0  # vitória pessoa
    mv = 0  # vitória máquina
    emp = 0  # empate

    if p == 1:  # pedra
        if m == 1:
            print("Pessoa x Máquina")
            print(" Pedra x Pedra\nIsso é um empate")
            emp += 1
        elif m == 2:
            print("Pessoa x Máquina")
            print(" Pedra x Papel\nPonto para a máquina!")
            mv += 1
        elif m == 3:
            print("Pessoa x Máquina")
            print(" Pedra x Tesoura\nPonto para a pessoa!")
            pv += 1
    elif p == 2:  # papel
        if m == 1:
            print("Pessoa x Máquina")
            print(" Papel x Pedra = Ponto para pessoa!")
            pv += 1
        elif m == 2:
            print("Pessoa x Máquina")
            print(" Papel x Papel = Isso é um empate")
            emp += 1
        elif m == 3:
            print("Pessoa x Máquina")
            print(" Papel x Tesoura = Ponto para a máquina!")
            mv += 1
    elif p == 3:  # tesoura
        if m == 1:
            print(" Pessoa x Máquina")
            print("Tesoura x Pedra = Ponto para a máquina!")
            mv += 1
        elif m == 2:
            print(" Pessoa x Máquina")
            print("Tesoura x Papel = Ponto para a pessoa!")
            pv += 1
        elif m == 3:
            print(" Pessoa x Máquina")
            print("Tesoura x Tesoura = Isso é um empate")
            emp += 1
    print("-" * 25)
    resultado = {'vitória pessoa': pv, 'vitória máquina': mv, 'empate': emp}
    return(resultado)


# PROGRAMA PRINCIPAL
print("***JOKENPÔ***")
pv = 0  # vitória pessoa
mv = 0  # vitória máquina
emp = 0  # empate
cont_j = 0  # contador de total de jogos

while True:
    menu()
    pessoa = validacao_jokenpo("Escolha sua jogada! ")
    if pessoa == 0:
        print("Encerrando...")
        break
    else:
        print("JO")
        sleep(0.5)
        print("KEN")
        sleep(0.5)
        print("PO!!!")

    maquina = randint(1, 3)
    jogo = jokenpo(pessoa, maquina)
    pv += jogo['vitória pessoa']
    mv += jogo['vitória máquina']
    emp += jogo['empate']
    cont_j += 1
    sleep(1.5)

print(
    f"Total de jogos: {cont_j}\nVitórias pessoa: {pv}\nVitórias máquina: {mv}\nEmpates: {emp}")


# 1- JOGO CONTÍNUO ATÉ A PESSOA DECIDIR SAIR;
# 2- TRABLHAR ESTATÍSTICAS, COMO PORCENTAGEM DE VITÓRIAS E EMPATES, JOGADAS MAIS ESCOLHIDAS E AFINS
