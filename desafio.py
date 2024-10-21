menu = """
Selecione uma operação:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("Bem vindo ao banco DIO!")
while True:

    opcao = input(menu)

    if opcao == "1":
        valor_str = input("Informe o valor desejado do depósito: ")
        valor_str = valor_str.replace(",", ".")
        valor = float(valor_str)

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor_str = input("Informe o valor desejado do depósito: ")
        valor_str = valor_str.replace(",", ".")
        valor = float(valor_str)

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        texto_extrato = " EXTRATO "
        linha = ""
        print(texto_extrato.center(41, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(linha.center(41, "="))

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")