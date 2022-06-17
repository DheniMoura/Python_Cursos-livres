# leia 5 números e mostre qual é o maior e o menor peso lido.
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso (em Kg) da {i}° pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi {maior}Kg")
print(f"O menor peso lido foi {menor}Kg")
