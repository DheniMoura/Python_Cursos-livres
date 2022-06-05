'''Calcule a soma entre todos os num ímpares que são múltiplos de 3 e que estão entre 1 e 500'''

soma = 0
count = 0
for i in range(1, 501, 2):
    if (i % 3 == 0):
        soma += i
        count += 1
print("A soma dos impares divisiveis por tres, entre 0 e 500 = ", soma)
print(f"Foram somados {count} numeros")
print("Fim")
