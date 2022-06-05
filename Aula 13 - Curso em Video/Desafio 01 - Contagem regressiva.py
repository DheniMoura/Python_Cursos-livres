'''Faça um programa que mostre na tela uma contagem regressiva 
indo de 10 até 0 com 1 segundo de pausa entre eles'''

from time import sleep

for i in range (10,-1,-1):
  print(i)
  sleep(1)
print("ACABOU!!")