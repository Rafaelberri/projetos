pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Bernardino',
    'idade' : 18,
    'altura' : 1.96,
    'endereços': [
        {'rua': 'tal tal', 'número': 961}
                  
    ]





}
print(pessoa['endereços'])
'''
chave = 'nome'


pessoa[chave] = ' Rafael'
pessoa['sobrenome'] = 'Bernardino'



print(pessoa)

pessoa[chave] = 'Maria'

del pessoa ['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get ('sobrenome') is None:
    print('Não possui')

else:
    print(pessoa['sobrenome'])

'''