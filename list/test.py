import os 

lista = []

while True:
    print("Escolha uma opção da lista")
    opcao = input(" (i)nserir, (a)pagar, (v)isualizar")

    if opcao == 'i':
        os.system("clear")
        valor = input("Coloque o item a ser inserido: ")
        lista.append(valor)

    elif opcao == "a":
        indice_str = input("Escolha o indice a ser apagado: ")

    try:
        indice = int(indice_str)
        del lista[indice]

    except:
        print("Não foi possivel apagar o item")