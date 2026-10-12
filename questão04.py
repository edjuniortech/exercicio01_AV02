def calcular_saldo(saldo, valor, operacao):
    if operacao == "deposito":
        return saldo + valor
    elif operacao == "saque":
        return saldo - valor

saldo = float(input("Digite o saldo atual: "))
valor = float(input("Digite o valor da operação: "))
operacao = input("Digite a operação (deposito ou saque): ")

novo_saldo = calcular_saldo(saldo, valor, operacao)

print("Novo saldo:", novo_saldo)
