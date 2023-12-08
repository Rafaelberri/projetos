def calcular_primeiro_digito(cpf):
    # Remover pontos e traço do CPF
    cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]

    # Calcular a soma dos produtos
    soma = sum(cpf_numeros[i] * (10 - i) for i in range(9))

    # Calcular o resultado final
    resultado = soma * 10 % 11

    # Verificar se o resultado é maior que 9
    if resultado > 9:
        return 0
    else:
        return resultado

# Exemplo de uso
cpf = "850.333.650-29"
primeiro_digito = calcular_primeiro_digito(cpf)
print(f"O primeiro dígito do CPF {cpf} é {primeiro_digito}")
