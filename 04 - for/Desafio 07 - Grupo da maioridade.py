'''
Crie um programa que leia o ano de nascimento de sete pessoas.<br>
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date  # biblioteca para obter a data atual

atual = date.today().year  # obtém o ano atual
menor = 0
maior = 0

for i in range(1, 8):
    ano_de_nascimento = int(
        input(f"Digite o ano de nascimento da {i}° pessoa: "))
    idade = atual - ano_de_nascimento

    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f"{maior} pessoas são maior de idade e {menor} pessoas são menor de idade")
