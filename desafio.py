import textwrap
from datetime import datetime

def menu():
    menu_texto = """\n
        ============= MENU =============

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair

    => """
    return input(textwrap.dedent(menu_texto))

def entrada_valor(mensagem):
    while True:
        try:
            valor_str = input(mensagem)
            valor = float(valor_str.replace(",", "."))
            if valor > 0:
                return valor
            else:
                print("Informe um valor positivo!")
        except ValueError:
            print("Valor inválido. Tente novamente.")

def depositar(saldo, valor, extrato, /):
    saldo += valor
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato += f"{data_hora} - Depósito: R$ {valor:.2f}\n"
    print("\n")
    print(" Depósito realizado com sucesso! ".center(41, "="))
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n--- Operação falhou! Você não tem saldo suficiente. ---")
    elif valor > limite:
        print("\n--- Operação falhou! O valor do saque excede o limite. ---")
    elif numero_saques >= limite_saques:
        print("\n--- Operação falhou! Número máximo de saques excedido. ---")
    else:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_hora} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n")
        print(" Saque realizado com sucesso! ".center(41, "="))
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n")
    print(" EXTRATO ".center(41, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}")
    print("".center(41, "="))

def validar_cpf(cpf):
    # Primeiro, verificamos se o CPF tem 11 dígitos e se não são todos iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verifica se os dígitos calculados conferem com os últimos dois dígitos do CPF
    return cpf[-2:] == f"{digito1}{digito2}"

def criar_usuario(usuarios):
    while True:
        cpf = input("Informe o CPF: ")
        # Remove pontos e hífens do CPF
        cpf = cpf.replace(".", "").replace("-", "")
        
        if len(cpf) != 11:
            print("\n--- CPF inválido! O CPF deve conter 11 dígitos. ---")
            continue
        
        if any(u['cpf'] == cpf for u in usuarios):
            print("\n--- Já existe usuário com esse CPF! ---")
            return

        if not validar_cpf(cpf):
            print("\n--- CPF inválido! Tente novamente. ---")
            continue

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")
        
        usuarios.append({
            "nome": nome, 
            "data_nascimento": data_nascimento, 
            "cpf": cpf, 
            "endereco": endereco
        })
        print(" Usuário criado com sucesso! ".center(41, "="))
        break

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print("\n")
        print(" Conta criada com sucesso! ".center(41, "="))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n--- Usuário não encontrado. ---")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta registrada.")
        return
    print("\n")
    print(" CONTAS ".center(41, "="), "\n")
    for i, conta in enumerate(contas):
        if i != 0:
            print("".center(41, "-"), "\n")
        print(f"Agência: {conta['agencia']}\nConta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}\n")
    print("".center(41, "="))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor = entrada_valor("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = entrada_valor("Informe o valor do saque: ")
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            criar_usuario(usuarios)
        elif opcao == "0":
            break
        else:
            print("Operação inválida, tente novamente.")

main()
