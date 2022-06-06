# Ler um num inteiro e dizer se é primo ou não
# Obs. não considerar tratamento de excessão para entrada de dados

num = int(input("Digite um número inteiro e positivo "))

teste = 0
count = 0
for i in range(num, 1, -1):
    if num % i == 0:
        teste = num / i
        count += 1
if count == 1:
    print(f"O numero {num} é primo")
else:
    print(
        f"O numero {num} não é primo e foi divisivel {count + 1} vezes entre 1 e ele mesmo")
