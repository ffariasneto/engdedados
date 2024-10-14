from datetime import datetime
from clients import client
from accounts import account
from movements import deposit, withdraw, check_movements


reg_clients = []
reg_accounts = []
extract = []
numb_withdraw = 0
limit_withdraw = 3
movements = []


while True:
    print("""
    Seja bem-vindo(a) ao FTi Bank!
    Escolha uma das opções abaixo: 

    [1] Cadastrar Cliente
    [2] Cadastrar Conta
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Movimentações
    [0] Sair
    """)
    main = input(": -> ")

    if main == "1":
        client(reg_clients)

    elif main == "2":
        account(reg_clients, reg_accounts)

    elif main == "3":
        cpf = input("Informe o CPF do cliente para depósito: ")
        value_deposit = float(input("Informe o valor de depósito: "))
        deposit(cpf, reg_accounts, value=value_deposit, extract=extract, movements=movements)

    elif main == "4":
        cpf = input("Informe o CPF do cliente para saque: ")
        value_withdraw = float(input("Informe o valor de saque: "))
        withdraw(cpf, reg_accounts, value=value_withdraw, extract=extract, limit=500, numb_withdraw=numb_withdraw, limit_withdraw=limit_withdraw, movements=movements)

    elif main == "5":
        print("--- Extrato ---")
        for item in extract:
            print(item)

    elif main == "6":
        print("--- Movimentações ---")
        total_movements = check_movements(movements)
        print(f"Total de movimentações do dia: {total_movements}")
        
    elif main == "0":
        print("Obrigado por utilizar o FTi Bank")
        break
    else:
        print("Opção inválida. Tente novamente.")
