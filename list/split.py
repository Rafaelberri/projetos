#split e join com list e str
# split divide uma string
# join une uma string

frase = "Olha só que coisa  ,  interessante"
frase2= "Muito interessante"

lista_palavra = frase.split(',')


print(lista_palavra)




for i, frase in enumerate(lista_palavra):
    lista_palavra[i] = lista_palavra[i].strip() # O strip é uma função que corta os espaços

print(lista_palavra)
