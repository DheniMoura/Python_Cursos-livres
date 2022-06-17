'''Desenvolva um programa que leia seis números inteiros e 
mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o
'''
# sem tratamento de dados de entrada
soma = 0
cont = 0
for i in range(0, 6):
    n = int(input("Digite um número inteiro "))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f"A soma dos {cont} numeros pares digitados é {soma}")
