quant_coluna = 5
quant_linha = 5

linha = 1 

while linha <= quant_linha:
    coluna = 1

    while coluna <= quant_coluna:
        print(f"{coluna=} {linha = }")
        coluna += 1
    linha +=1
    
print("Fim")