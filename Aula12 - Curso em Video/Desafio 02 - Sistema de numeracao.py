n = int(input("Digite um número inteiro: "))
print("Converter para: ")
print(" [1] BINÁRIO\n [2] OCTAL\n [3] HEXADECIMAL\n Para sair digite outro número")
e = int(input("Digite sua escolha: "))

if e == 1:
  print(f'{n} decimal = {bin(n)[2:]} binário')
elif e == 2:
  print(f'{n} decimal = {oct(n)[2:]} octal')
elif e == 3:
  print(f'{n} decimal = {hex(n)[2:]} hexadecimal')
else:
  print('Saindo...')
