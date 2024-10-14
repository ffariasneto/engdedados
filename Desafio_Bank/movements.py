from datetime import datetime

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