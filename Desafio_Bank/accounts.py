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