#define a string que será calculada
frase = 'aaabbcdddddd'
#define o indice como 0
i = 0
#inicio da contagem
qtd_apareceu_mais = 0
#define a var para mostrar a letra que apareceu mais vezes
letra_mais_vezes = ' '
# Laço inicia enquanto houver valor maior que o indice, caso não seja o laço não será executado
while i < len(frase):
# Começa a contagem a partir do inicio da frase
    letra_atual = frase[i]
# Boolean, onde faz o inicio da contagem a partir do inicio da frase e vai somando de letra em letra
    if letra_atual == '':
        i += 1
        continue
    #Define a quantidade de caracteres da frase
    qtd_atual =frase.count(letra_atual)
    # se a quantidade for menor ou igual a zero
    if qtd_apareceu_mais <= qtd_atual:
        #quantidade igual a 0
        qtd_apareceu_mais = qtd_atual
        letra_mais_vezes = qtd_atual
#Soma + 1 no indice
        i += 1

        print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais}x'
) 