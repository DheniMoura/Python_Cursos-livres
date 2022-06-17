# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

num = []
for i in range(0, 3):
    num.append(float(input('Digite um número: ')))

maior = max(num)
menor = min(num)

print('maior: ', maior)
print('menor: ', menor)
