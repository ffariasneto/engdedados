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