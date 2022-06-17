#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

f = str(input("Digite uma frase: ")).strip().upper() #.strip() para remover os espaços do início e do fim da Frase
print(f"Você digitou a frase {f}")

p = f.split() #.split() para transformar a frase em uma lista de Palavras separadas pelo espaço
j = ''.join(p) #.join() para Juntar as palavras, sem espaços
i = j[::-1] #Inverte a frase, letra por letra

'''
i = '' #Inverso
for letra in range(len(j) -1, -1, -1): #aqui percorre letra por letra para inverter a frase
  i += j[letra]
print(i, end=" -> ")'''

if i == j: #confere se a frase original é igual a frase invertida
  print("é palindromo!")
else:
  print("não é palindromo")