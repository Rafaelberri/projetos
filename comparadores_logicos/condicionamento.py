entrar = input("Digite (E)ntrar oara entrar ou (S)air para sair")


if entrar == "E":
    usuariologin = input("Insira o nome de usuario: ")
    senhalogin =input("Digite a senha de login: ")
    usuario = "admin"
    senha = "123456"

    if usuariologin == usuario and senhalogin == senha:

        print("Bem vindo ao sistema")
    else: 
        print("Usuario ou senha incorreto!")

elif entrar == "S":
    print("Sair")

else:
    print("Não foi possivel autenticar o sistema")
