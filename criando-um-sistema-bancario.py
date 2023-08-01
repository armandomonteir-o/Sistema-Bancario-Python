## depósito, saque e extrato

## deposíto = valor positivo; armazenado em uma variável e exibido na opção de extrato
##saque = permite 3 saques diarios com limite maximo de 500 por saque; em caso do usuario n ter saldo em conta, exibir
## uma mensagem informando que não será possível sacar o dinheiro por falta de saldo; saques devem ser armazenados em
## uma variável e serem exibidos na opção de extrato
##extrato = lista todas os depositos e saques realizados na conta e no fim da listagem o saldo atual da conta.
##os valores devem ser exibidos utilizando o formato R$ xxx.xx

menu = '''         Bem vindo ao Banco Nacional

-----------------Escolha sua Operação-----------------
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
------------------------------------------------------'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3




while True:

    opção = input(menu)

    if opção == "1":
        valor = float(input("Informe o valor do depósito "))

        if valor >0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso.\n")

        else:
            print("Operação não realizada. Por favor, tente novamente. ")

    elif opção == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada. Você não possui saldo suficiente. ")

        if excedeu_limite:
            print("Operação não realizada. Você não possui limite suficiente. ")

        if excedeu_saques:
            print("Operação não realizada. Você já atingiu o limite de saques disponíveis ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso\n")

        else:
            print("Operação não realizada. O valor informado é inválido. ")

    elif opção == "3":
        print("\n---------------------Extrato---------------------")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("------------------------------------------")

    elif opção == "4":
        print("Obrigado por utilizar nossos serviços. ")
        break

    else:
        print("Operação não realizada. Por favor tente novamente ")





      



