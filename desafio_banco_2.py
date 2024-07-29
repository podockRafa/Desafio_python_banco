import textwrap



def menu():

    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tTransferência
    [4]\tExtrato
    [5]\tNovo Usuário
    [6]\tNova Conta
    [7]\tListar contas
    [0]\tSair
    
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_transacoes):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_transacoes = numero_saques >= limite_transacoes

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_transacoes:
        print("\n@@@ Operação falhou! Número máximo de transações excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

    # excedeu_saldo = valor > saldo
    #
    # excedeu_limite = valor > limite
    #
    # excedeu_saques = numero_saques >= LIMITE_SAQUES
    #
    # if excedeu_saldo:
    #     print("Operação falhou! Você não tem saldo suficiente.")
    #
    # elif excedeu_limite:
    #     print("Operação falhou! O valor do saque excede o limite do saque. Valor máximo R$ 500,00")
    #
    # elif excedeu_saques:
    #     print("Operação falhou! Número máximo de saques excedido.")
    #
    # elif valor > 0:
    #     saldo -= valor
    #     extrato += f"Saque: R$ {valor:.2f}\n"
    #     numero_saques += 1
    #     print("Saque efetuado com sucesso!")
    #
    # else:
    #     print("Operação falhou! O valor informado é inválido.")

def transferir(saldo, valor, extrato, limite, numero_transferencias, limite_transacoes):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_transacoes = numero_transferencias >= limite_transacoes

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_transacoes:
        print("\n@@@ Operação falhou! Número máximo de transações excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Transferência:\t\tR$ {valor:.2f}\n"
        numero_transferencias += 1
        print("\n=== Transferência realizada com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato
            # excedeu_saldo = valor > saldo
            #
            # excedeu_limite = valor > limite
            #
            # excedeu_transferencia = numero_transferencia >= LIMITE_TRANSFERENCIAS
            #
            # if excedeu_saldo:
            #     print("Operação falhou! Você não tem saldo suficiente.")
            #
            # elif excedeu_limite:
            #     print("Operação falhou! O valor da transferência excede o limite do saque. Valor máximo R$ 500,00")
            #
            # elif excedeu_transferencia:
            #     print("Operação falhou! Número máximo de transferências excedido.")
            #
            # elif valor > 0:
            #     saldo -= valor
            #     extrato += f"Transferência: R$ {valor:.2f}\n"
            #     numero_transferencia += 1
            #     print("Transferência efetuada com sucesso!")
            #
            # else:
            #     print("Operação falhou! O valor informado é inválido.")

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

    # print("\n================ EXTRATO ================")
    # print("\nTRANSAÇÕES EFETUADAS:")
    # print("Não foram realizadas movimentações." if not extrato else extrato)
    # print(f"\nSaldo: R$ {saldo:.2f}")
    # print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_TRANSACAO = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_transferencias = 0
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_TRANSACAO)


        elif opcao == "3":
            valor = float(input("Informe o valor da sua transferência: "))

            saldo, extrato = transferir(saldo, valor, extrato, limite, numero_transferencias, LIMITE_TRANSACAO)


        elif opcao == "4":
            exibir_extrato(saldo, extrato=extrato)


        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "7":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()