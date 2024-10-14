def registrar_movimentacao(tipo, valor):
    extrato.append(f"{tipo}: R$ {valor}")

menu = """

Seja bem-vindo(a) ao FTi Bank!
Escolha uma das opções abaixo: 

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        vlr = float(input("Digite o valor que deseja depositar: "))
        if vlr <= 0:
            print("Valor não pode ser igual a 0 (zero) ou negativo!\n")
        else:
            saldo += vlr
            registrar_movimentacao("Depósito - R$", vlr)
            print("Depósito atualizado com sucesso!\n")
            print(f"Saldo atualizado: R$ {saldo:.2f}")

    
    elif opcao == "2":
        vlr = float(input("Digite o valor que deseja sacar: "))
        if vlr > limite:
            print("Valor de saque acima do permitido!\n")
        elif numero_saques > 2:
            print("Limite de saques diário atingido, volte amanhã!\n")
        elif saldo == 0:
            print("Saldo insuficiente!\n")
        else:
            saldo -= vlr
            registrar_movimentacao("Saque - R$", vlr)
            numero_saques += 1
            print("Saque realizado com sucesso!\n")
            print(f"Saldo atualizado: R$ {saldo:.2f}")
    
    elif opcao == "3":
        for mov in extrato:
            print(mov)
        print(f"Saldo atualizado: R$ {saldo:.2f}")
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")