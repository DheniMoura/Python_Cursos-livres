'''Desenvolva um programa que leia seis números inteiros e 
mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o
'''
# sem tratamento de dados de entrada

# Essa é uma opção de código que considera armazenar quais foram os números digitados, e quais foram os números somados
soma = 0
n = []
pares = []
cont = 0
for i in range(0, 6):
    n.append(int(input("Digite um número inteiro ")))
    if n[i] % 2 == 0:
        cont += 1
        soma += n[i]
        pares.append(n[i])
print(f"Foram digitados {cont} numeros pares, são eles: {pares}")
print(f"A soma desses numeros é igual a {soma}")
