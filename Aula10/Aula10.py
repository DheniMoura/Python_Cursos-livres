n1 = float(input('Digite a primeira nota: (0 a 10)'))
n2 = float(input('Digite a segunda nota: (0 a 10)'))
m = (n1 + n2)/2

print('média: {:.1f}'.format(m))
if m < 3:
    print('Aluno reprovado por nota')
elif m < 7:
    print('Aluno em recuperação')
elif m > 10 or m < 0:
    print('Você digitou uma nota errada?')
else:
    print('Aluno aprovado por nota')


# c = int(input('Digite 1 se a condição for verdadeira'))
# print('Condição verdadeira' if c == 1 else 'Condição falsa')