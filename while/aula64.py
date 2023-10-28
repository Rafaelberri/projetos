nome = "Rafael Bernardino "

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    print(novo_nome)

print(novo_nome)