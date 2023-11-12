while True:
    valor1 = input("Insira o 1º número: ")
    valor2 = input("Insira o 2º número: ")
    operador = input("Insira o operador(+-/*): ")

    valor_valido = None

    try:
        valor1_float = float(valor1)
        valor2_float = float(valor2)
        valor_valido = True

    except:
        
        valor_valido = None

    if valor_valido is None:
        print("Um ou mais valores invalidos foram inseridos")
        continue
    operadores_validos = '/*+-'

    if operador not in operadores_validos:
        print("Insira uma expressão válida")

    if operador == '+':
        resultado = valor1_float + valor2_float
        print(resultado)

    elif operador == '-':
        resultado = valor1_float - valor2_float
        print (resultado)
    
    elif operador == "*":
        resultado = valor1_float * valor2_float
        print(resultado)

    elif operador == '/':
        resultado = valor1_float / valor2_float
        print(resultado)

        
    sair = input("Você deseja sair?(S)im para sair e(N)ão para continuar: ").lower().startswith('s')


    if sair is True:
        print("Saida com exito!")
        break
    
    elif sair is False:
        continue



