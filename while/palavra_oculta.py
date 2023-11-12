palavra_oculta = 'sorvete'
tentativa = 0
convertido = ''


while True:
    
    i = input ('Insira a letra: ')
    tentativa += 1
    
    if len(i) > 1:
        print ( 'Insira apenas uma letra!')
        continue
    
    if i in palavra_oculta:
        convertido += i
        print(convertido)
        tentativa -= 1
        

    if convertido == palavra_oculta:
        print(f"Você encontrou a palavra oculta {palavra_oculta}!")
        print(f"Você achou em {tentativa} tentativas !")
        break

