from datetime import datetime

def client(reg_clients):
    clients = {}
    cpf = input("Informe o CPF: ")

    for c in reg_clients:
        if c["CPF"] == cpf:
            print("Erro: CPF já cadastrado")
            return
    
    clients["CPF"] = cpf
    name = input("Digite o nome do cliente: ")
    clients["Nome"] = name
    date_birth = input("Informe a data de nascimento: ")
    clients["Data Nascimento"] = date_birth
    address = input("Informe o endereço -> (Log, Nº, Bairro, Cidade/UF): ")
    clients["Endereço"] = address
    
    reg_clients.append(clients)
    print("Cliente cadastrado com sucesso!")

def account(reg_clients, reg_accounts):
    accounts = {}
    cpf = input("Digite o CPF do cliente: ")

    for c in reg_clients:
        if c["CPF"] == cpf:
            accounts["Usuário"] = cpf
            account = int(input("Digite o número da conta: "))
            for a in reg_accounts:
                if a["Núm.Conta"] == account:
                    print("Conta já cadastrada!")
                    return
              
            accounts["Núm.Conta"] = account
            agency = "0001"
            accounts["Agência"] = agency
            balance = float(input("Digite o saldo inicial da conta: "))
            accounts["Saldo"] = balance

            reg_accounts.append(accounts)
            print("Conta cadastrada com sucesso!")
            return
    
    print("Erro: Cliente não encontrado.")

# Função para verificar o número de movimentações no dia
def check_movements(movements):
    today = datetime.now().date()
    movements_day = [mov for mov in movements if mov["Data"].date() == today]
    return len(movements_day)

# Função para realizar saques
def withdraw(cpf, reg_accounts, *, value, extract, limit, numb_withdraw, limit_withdraw, movements):
    # Verifica o número de movimentações do dia
    total_movements = check_movements(movements)
    if total_movements >= 10:
        print("Erro: Limite de 10 movimentações diárias atingido!")
        return
    
    # Localiza a conta pelo CPF
    for acc in reg_accounts:
        if acc["Usuário"] == cpf:
            balance = acc["Saldo"]
            
            # Verifica se o valor do saque é válido
            if value <= 0:
                print("Erro: O valor de saque deve ser maior que zero!")
                return

            # Verifica se o número de saques excedeu o limite
            if numb_withdraw >= limit_withdraw:
                print("Erro: Limite de saques diários atingidos!")
                return
            
            # Verifica se o valor de saque não excede o saldo e o limite
            if value > balance:
                print("Erro: Saldo insuficiente!")
                return
            elif value > limit:
                print(f"Erro: O valor de saque excede o limite permitido de R$ {limit}")
                return

            # Se passar em todas as verificações, realiza o saque
            acc["Saldo"] -= value
            extract.append(f"Saque de R$ {value:.2f}")
            movements.append({
                "Tipo": "Saque",
                "Valor": value,
                "Data": datetime.now()
            })
            numb_withdraw += 1
            print(f"Saque de R$ {value:.2f} realizado com sucesso!")
            return

    print("Erro: Cliente não encontrado.")

# Função para realizar depósitos
def deposit(cpf, reg_accounts, *, value, extract, movements):
    if value <= 0:
        print("Erro: O valor de depósito deve ser maior que zero!")
        return
    
    #Verifica o número de movimentações no dia
    total_movements = check_movements(movements)
    if total_movements >= 10:
        print("Erro: Limite de 10 movimentações diárias atingido!")
        return
    
    # Localiza a conta pelo CPF
    for acc in reg_accounts:
        if acc["Usuário"] == cpf:
            acc["Saldo"] += value
            extract.append(f"Depósito de R$ {value:.2f}")
            movements.append({
                "Tipo": "Depósito",
                "Valor": value,
                "Data": datetime.now()
            })
            print(f"Depósito de R$ {value:.2f} realizado com sucesso!")
            return
    
    print("Erro: Cliente não encontrado.")

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
