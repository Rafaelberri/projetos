nome = input("Insira o seu nome: ")
idade = input("Insira a sua idade: ")

if nome.strip() != "" and idade.strip() != "":
    print(f"O seu nome é: {nome}")
    print(f'O seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
    
    if " " in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")
    
else:
    print("Desculpe, você deixou campos vazios.")
