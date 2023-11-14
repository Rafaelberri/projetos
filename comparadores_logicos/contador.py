#string a ser calculado
frase = 'aaaaooo'

#define o indice como 0
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

#condição deve ser atendida enquanto houver algo na string
while i < len(frase):
    
    #iteração da string a partir do valor do indice
    letra_atual = frase[i]
    #se houver espaço na frase pular para próxima letra
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)