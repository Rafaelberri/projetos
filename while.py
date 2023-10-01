import random

print("Bem-vindo ao jogo. Você deve encontrar o número premiado de 1 a 20")
numero_premiado = random.randint(1, 20)  # Gera um número aleatório entre 1 e 20
tentativas = 0

while True:
    tentativa = input("Insira um número de 1 a 20: ")
    
    if not tentativa.isdigit():
        print("Entrada inválida. Por favor, insira um número válido.")
        continue

    numero = int(tentativa)
    
    if numero < 1 or numero > 20:
        print("Entrada inválida. O número deve estar entre 1 e 20.")
        continue

    tentativas += 1

    if numero == numero_premiado:
        print(f"Parabéns! Você encontrou o número premiado {numero_premiado} em {tentativas} tentativas.")
        break
    else:
        print("Você não encontrou. Tente novamente.")
