menu = """

[1] Depositar
[2] Sacar
[3] Transferência
[4] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_transferencia = 0
limite_transferencia = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito efetuado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite do saque. Valor máximo R$ 500,00")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "3":
        valor = float(input("Informe o valor da sua transferência: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_transferencia = numero_transferencia >= limite_transferencia

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor da transferência excede o limite do saque. Valor máximo R$ 500,00")

        elif excedeu_transferencia:
            print("Operação falhou! Número máximo de transferências excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Transferência: R$ {valor:.2f}\n"
            numero_transferencia += 1
            print("Transferência efetuada com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "4":
        print("\n================ EXTRATO ================")
        print("\nTRANSAÇÕES EFETUADAS:")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")



    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")