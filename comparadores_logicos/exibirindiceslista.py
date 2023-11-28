lista = ['Rafael', 'Bernardino', 'Riveira']


for codigo_lista in lista:
    if codigo_lista == 0 and lista[0]:
        codigo_lista += 1
        lista[0] += 1

    print(f'{codigo_lista},{lista}')
