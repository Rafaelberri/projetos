

lista = []

while True:
    print (f'Bem vindo a lista de compras. Insira um número para selecionar uma opção: \n'
          f'1.Adicionar item \n'
          f'2.Remover item \n'
          f'3.Consultar Lista\n'
          f'4. Sair')
    
    escolha = input("\nEscolha uma opção (1-4): ")

    if escolha == "1":
        item_adicionado = input("Insira o item que deseja adicionar a sua lista: ")
        lista.append(item_adicionado)
        print(f'O item {item_adicionado} foi adicionado em sua lista com sucesso!')

    elif escolha == "2":
        for i, item in enumerate(lista):
            print(f"Insira o item que deseja remover: \n"
              f"{lista}")
            remover = input("Digite o código: ")
            lista.pop(remover)
            print(f"O item {item} foi removido com sucesso! Segue a nova lista: \n {lista} ")

            if remover not in i:
                print("Digite um código válido!")

    elif escolha == "3":
        print(f'Os seguintes itens da sua lista são: {lista}')
        

    elif escolha == "4":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")


