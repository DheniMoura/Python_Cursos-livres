'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. '''

num = []
for i in range(0,2):
    num.append(int(input(f"Digite o {i+1}° valor: ")))

menu = 4
while menu != 5:
    print("=" * 15, "MENU", "=" * 15)
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    menu = int(input("Digite a sua escolha: "))

    if menu == 1:
      soma = num[0] + num[1]
      print(f"{num[0]} + {num[1]} = {soma}")
    elif menu == 2:
      produto = num[0] * num[1]
      print(f"{num[0]} x {num[1]} = {produto}")
    elif menu == 3:
      if num[0] == num[1]:
        print(f"{num[0]} = {num[1]} (são iguais)")      
      elif num[0] < num[1]:
        print(f"{num[0]} < {num[1]} ({num[1]} é maior)")
      else:
        print(f"{num[1]} < {num[0]} ({num[0]} é maior)")
    elif menu == 4:
      num = []
      for i in range(0,2):
        num.append(int(input(f"Digite o {i+1}° valor: ")))
    elif menu == 5:
      print("Encerrando...")
    else:
      print("Opção inválida, digite novamente ")

print("Volte sempre!")