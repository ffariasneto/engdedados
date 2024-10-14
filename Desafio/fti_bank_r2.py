class Cliente:
    def __init__(self, nome, cpf, endereco, cidade, uf):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf
        
# class Conta(Cliente):
#     def __init__(self, nome, cpf, endereco, cidade, uf, numero, saldo):
#         super().__init__(nome, cpf, endereco, cidade, uf)
#         self.numero = numero
#         self.saldo = saldo
#         self.resumo = []

clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o cpf do cliente: ")
    endereco = input("Digite o endereco e o bairro do cliente: ")
    cidade = input("Digite a Cidade do cliente: ")
    uf = input("Digite a sigla do Estado do cliente: ")

    cliente = Cliente(nome, cpf, endereco, cidade, uf)

    cliente_dict = {
        "Nome": cliente.nome,
        "CPF": cliente.cpf,
        "Endereço": cliente.endereco,
        "Cidade": cliente.cidade,
        "UF": cliente.uf
    }

    clientes.append(cliente_dict)

cadastrar_cliente()
print(clientes)

# menu = """

# Seja bem-vindo(a) ao FTi Bank!
# Escolha uma das opções abaixo: 

# [1] Cadastrar Cliente
# [2] Cadastrar Conta Bancária 
# [3] Depositar
# [4] Sacar
# [5] Extrato
# [0] Sair

# => """
# print(menu)
