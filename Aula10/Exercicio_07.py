#cada um dos lados precisa menor que a soma dos outros dois lados.
a = float(input('Lado 1 (cm): '))
b = float(input('Lado 2 (cm): '))
c = float(input('Lado 3 (cm): '))

if a + b > c and a + c > b and b + c > a:
    print('Triângulo feito!') 
else:
    print('Não forma um triângulo.') 