try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2
    print("Resultado da divisão:", resultado)

except ValueError:
    print("Entrada inválida! Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero!")
