#entrada de hexadecimal

# Solicita ao usuário que insira uma string que represente um número inteiro
input_string = input("Insira um número inteiro: ")

# Tenta converter a string em um número inteiro
while True:
    input_string = input("Insira um número inteiro: ")

    try:
        numero_inteiro = int(input_string)
        print("Número inteiro convertido:", numero_inteiro)
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Erro: A entrada não é um número inteiro válido. Tente novamente.")
