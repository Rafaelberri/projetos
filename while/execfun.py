print(1*2*3*4*5)

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
multiplicacao = multiplicar(1,2,3,4,5)

print(multiplicacao)

def par_impar(numero):
    return numero % 2 == 0

print(par_impar(2))
print(par_impar(3))
