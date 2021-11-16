print('se não souber os operadores digite 1')
operador = (input('Digite o operador: ')) # Variavel feita para capturar o operador, note que esta pegando ela no tipo STRING
if operador == str(1): # Se o usuario digitar 1 vai imprimir as seguintes coisas:
    print('Multiplicação: *\nDivisão: /\nSoma: +\nSubtração: -')
    input('\n\nDigite qualquer coisa para continuar')
    operador = (input('\nDigite o operador: '))
n1 = float(input('Digite o primeiro numero: ')) 
n2 = float(input('Digite o segundo numero: '))

# Aqui nesse ponto do codigo, devemos lembrar que a variavel operador esta em STRING, então no if, não vamos colocar operador == *, e sim operador == '*'.
# Pois só assim analizaremos se ele escreveu o operador, pois sem os ' ' não fica uma string.
if operador == '*': 
    print('O resultado é: ' , n1*n2)
    input('Precione qualquer coisa para continuar')
elif operador == '+':
    print('O resultado é: ' , n1+n2)
    input('Precione qualquer coisa para continuar')
elif operador == '/':
    print('O resultado é: ' , n1/n2)
    input('Precione qualquer coisa para continuar')
elif operador == '-':
    print('O resultado é: ' , n1-n2)
    input('Precione qualquer coisa para continuar')
else:
    print('Operador inválido!')
    
                                                        #Feito por Eduardo Fantim, 2021, 15 anos.
