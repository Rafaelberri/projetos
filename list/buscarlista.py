nome_lista = ['nome1', 'nome2', 'nome3']
indices = range(len(nome_lista))

for indice in indices : 
    print(indice, nome_lista[indice]), type(nome_lista[indice])
    
    if range(indice) == len(indices):
        break

nome_lista.append(70)

print(nome_lista)


for indice in indices : 
    print(indice, nome_lista[indice]), type(nome_lista[indice])
    
    if range(indice) == len(indices):
        break