lista = ['nome0', 'nome1', 'nome2']
lista.append('nome3')

for codigo, item in enumerate(lista):
    print(codigo, item)

    if codigo == len(lista) - 1:
        
        valor1= input('Insira o código do produto a ser verificado: ')

        valorint = int(valor1)

        print(f'O item da lista a ser selecionado é {lista[valorint]}')
