# Lista para armazenar os clientes
clientes = []

# Função para adicionar cliente
def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    cpf = input("Digite o CPF do cliente: ")

    cliente = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'cpf': cpf
    }
    clientes.append(cliente)
    print(f"Cliente '{nome}' adicionado com sucesso!\n")

# Função para listar todos os clientes
def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        print("\nLista de clientes:")
        for i, cliente in enumerate(clientes):
            print(f"{i+1}. {cliente['nome']}")
        print()

# Função para puxar informações de um cliente específico
def puxar_informacoes_cliente():
    nome_cliente = input("Digite o nome do cliente que deseja buscar: ")
    for cliente in clientes:
        if cliente['nome'].lower() == nome_cliente.lower():
            print(f"\nInformações do cliente '{nome_cliente}':")
            print(f"Nome: {cliente['nome']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"E-mail: {cliente['email']}")
            print(f"CPF: {cliente['cpf']}\n")
            return
    print(f"Cliente '{nome_cliente}' não encontrado.\n")

# Menu interativo
def menu():
    while True:
        print("1. Adicionar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            puxar_informacoes_cliente()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o menu
menu()
