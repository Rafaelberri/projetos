'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados

'''
x = 9
y = 3
def escopo():
    global x
    x = 5 
    y = 7

    print(f' Saida do escopo : {x} {y}')
    
    def other_escopo():
        print("saiu saporra")

    other_escopo()
        

escopo()

print(x,y)

