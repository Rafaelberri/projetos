
#Introdução ao despacotamento de listas
nome = ['João', 'Maria', 'Rafael', 'Kleber', 'Ana', 'Julio']

#Define o Valor da lista 0 como nome0 e o resto como '_'
nome0, *_ = nome

#Saida de dados com o valor de nome0 + saida de'_' com indice 4 da lista resto
print (nome0, _[4])