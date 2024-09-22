menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Qual valor deseja depositar: "))

        if deposito > 0:
            print(f"Depósito de R$ {deposito:.2f} realizado!")
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Valor inválido!")

    elif opcao == "2":
        saque = float(input("Informe o valor do saque: "))

        exedeu_saldo = saque > saldo

        exedeu_limite = saque > limite

        exedeu_saques = numero_saque >= LIMITE_SAQUES

        if exedeu_saldo:
            print("Operação falhou! Você não tem saldo o suficiente.")

        elif exedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif exedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saldo:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido")
            
    elif opcao == "3":
        print("\n****************** Extrato ******************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*********************************************")

    elif opcao == "0":
        print("Obrigado por usar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada")
