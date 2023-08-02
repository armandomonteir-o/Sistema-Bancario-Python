from typing import List, Tuple

usuarios = []
contas = []
numero_conta = 1

def cadastrar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str) -> None:
    global usuarios
    cpf = ''.join(filter(str.isdigit, cpf))
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado")
        return
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso")

def cadastrar_conta(usuario_cpf: str) -> None:
    global contas, numero_conta
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == usuario_cpf), None)
    if not usuario:
        print("Usuário não encontrado")
        return
    contas.append({
        'agencia': '0001',
        'numero': numero_conta,
        'usuario': usuario
    })
    print(f"Conta {numero_conta} criada com sucesso")
    numero_conta += 1

def deposito(saldo: float, valor: float, extrato_str: str) -> Tuple[float, str]:
    if valor > 0:
        saldo += valor
        extrato_str += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso.\n")
    else:
        print("Operação não realizada. Por favor, tente novamente. ")
    return saldo, extrato_str

def saque(*, saldo: float, valor: float, extrato_str: str, limite: float, numero_saques: int, limite_saques: int) -> Tuple[float, str]:
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação não realizada. Você não possui saldo suficiente. ")
    if excedeu_limite:
        print("Operação não realizada. Você não possui limite suficiente. ")
    if excedeu_saques:
        print("Operação não realizada. Você já atingiu o limite de saques disponíveis ")
    elif valor > 0:
        saldo -= valor
        extrato_str += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso\n")
    else:
        print("Operação não realizada. O valor informado é inválido. ")
    return saldo, extrato_str

def extrato(saldo: float, *, extrato_str: str) -> None:
    print("\n---------------------Extrato---------------------")
    print("Não foram realizadas movimentações. " if not extrato_str else extrato_str)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("------------------------------------------")

menu = '''         Bem vindo ao Banco Nacional

-----------------Escolha sua Operação-----------------
[1] Depósito
[2] Saque
[3] Extrato
[4] Cadastrar Usuário
[5] Cadastrar Conta Corrente
[6] Sair
------------------------------------------------------'''

saldo = 0
limite = 500
extrato_str = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "1":
        valor = float(input("Informe o valor do depósito "))
        saldo, extrato_str = deposito(saldo, valor, extrato_str)

    elif opção == "2":
        if numero_saques >= LIMITE_SAQUES:
            print("Operação não realizada. Você já atingiu o limite de saques disponíveis ")
            continue
        
        valor = float(input("Informe o valor do saque: "))
        
        saldo, extrato_str = saque(saldo=saldo, valor=valor, extrato_str=extrato_str, limite=limite,
                               numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
        numero_saques += 1

    elif opção == "3":
        extrato(saldo=saldo, extrato_str=extrato_str)

    elif opção == "4":
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento do usuário (dd/mm/aaaa): ")
        cpf = input("Informe o CPF do usuário (somente números): ")
        endereco = input("Informe o endereço do usuário (logradouro, número, bairro, cidade/sigla estado): ")
        cadastrar_usuario(nome=nome, data_nascimento=data_nascimento,
                          cpf=cpf, endereco=endereco)

    elif opção == "5":
        cpf = input("Informe o CPF do usuário (somente números): ")
        cadastrar_conta(cpf)

    elif opção == "6":
        print("Obrigado por utilizar nossos serviços. ")
        break

    else:
        print("Operação não realizada. Por favor tente novamente ")
