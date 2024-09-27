def calculadora(num1, num2, operacao):
    """
    Função que realiza operações matemáticas com dois números.

    Parâmetros:
    num1 (float): Primeiro número.
    num2 (float): Segundo número.
    operacao (int): Operação a ser realizada:
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão

    Retorna:
    float: Resultado da operação ou 0 se a operação não for válida.
    """
    if operacao == 1:  # Soma
        return num1 + num2
    elif operacao == 2:  # Subtração
        return num1 - num2
    elif operacao == 3:  # Multiplicação
        return num1 * num2
    elif operacao == 4:  # Divisão
        if num2 != 0:  # Evita divisão por zero
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:  # Operação inválida
        return 0

# Exemplo de uso
resultado = calculadora(10, 5, 1)  # Soma
print("Resultado da soma:", resultado)

resultado = calculadora(10, 5, 2)  # Subtração
print("Resultado da subtração:", resultado)

resultado = calculadora(10, 5, 3)  # Multiplicação
print("Resultado da multiplicação:", resultado)

resultado = calculadora(10, 5, 4)  # Divisão
print("Resultado da divisão:", resultado)

resultado = calculadora(10, 5, 5)  # Operação inválida
print("Resultado de operação inválida:", resultado)

