print('se não souber os operadores digite 1')
operador = (input('Digite o operador: '))
if operador == str(1):
    print('Multiplicação: *\nDivisão: /\nSoma: +\nSubtração: -')
    input('\n\nDigite qualquer coisa para continuar')
    operador = (input('\nDigite o operador: '))
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
print('\n')
if operador == '*':
    print('O resultado é: ' , n1*n2)
elif operador == '+':
    print('O resultado é: ' , n1+n2)
elif operador == '/':
    print('O resultado é: ' , n1/n2)
elif operador == '-':
    print('O resultado é: ' , n1-n2)
else:
    print('Operador inválido!')