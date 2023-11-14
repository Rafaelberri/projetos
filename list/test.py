lista = ['Rafael',22,1.96,'25/03/2001']
lista2 = ['Bernardino', 'março']
lista.append('solteiro')
lista.pop(3)
lista.append(50)
lista.extend(lista2)
nome = lista[0]
sobrenome = lista2[0]
print(nome,sobrenome)