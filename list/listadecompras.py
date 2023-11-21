#Esse projeto tem como base criar uma lista, dando a possibilidade do usuario inserir,consultar e deletar itens da lista

def exibir_menu():
    print("\n1. Inserir item")
    print("2. Consultar lista")
    print("3. Deletar item")
    print("4. Sair")

def inserir_item(lista):
    novo_item = input("Digite o novo item: ")
    lista.append(novo_item)
    print(f"Item '{novo_item}' inserido com sucesso!")

def consultar_lista(lista):
    print("\nItens na lista:")
    for i, item in enumerate(lista):
        print(f"{i + 1}. {item}")

def deletar_item(lista):
    consultar_lista(lista)
    if not lista:
        print("A lista está vazia. Nada para deletar.")
        return

    try:
        indice = int(input("Digite o número do item que deseja deletar: ")) - 1
        if 0 <= indice < len(lista):
            item_deletado = lista.pop(indice)
            print(f"Item '{item_deletado}' deletado com sucesso!")
        else:
            print("Número de item inválido.")
    except ValueError:
        print("Digite um número válido.")

def main():
    minha_lista = []

    while True:
        exibir_menu()

        escolha = input("\nEscolha uma opção (1-4): ")

        if escolha == "1":
            inserir_item(minha_lista)
        elif escolha == "2":
            consultar_lista(minha_lista)
        elif escolha == "3":
            deletar_item(minha_lista)
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
