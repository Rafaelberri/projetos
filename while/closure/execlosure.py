# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicacao(multiplicador):
    def multiplicar(numero):
           return numero * multiplicador
    return multiplicar
    
duplicar = multiplicacao(2)
triplicar = multiplicacao(3)
quadruplicar = multiplicacao(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))


#teste 

resultado_duplicar = int(input("Digite um número para ser duplicado: "))


print(duplicar(resultado_duplicar))