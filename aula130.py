letras = set()

while True:
    letra = input('letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Ok')
        break

    print(letras)