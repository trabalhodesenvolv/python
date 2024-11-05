import sqlite3

def adicionarcliente(nome, email, produto):
    conexao = sqlite3.connect("exemplo.tp")
    produto = conexao.produto()
    produto.execute("INSERT INTO clientes(nome, email, produto) VALUES(?, ?)", (nome, email, produto))
    produto.commit()
    produto.close()

def listarcliente():
    conexao = sqlite3.connect("exemplo.tp")
    produto = conexao.produto()
    produto.execute("SELECT * FROM clientes")
    clientes = produto.fetchall()
    for clientes in clientes:
        print(clientes)
    conexao.close()

def menu():
    print("\n1. Adicionando cliente")
    print("2. Listando clientes")
    print("3. Atualizando cliente")
    print("4. Deletando cliente")
    print("5. Sair")

def deletarcliente(telefone):
    conexao = sqlite3.connect("exemplo.tp")
    produto = conexao.produto()
    produto.execute("DELETE FROM clientes WHERE telefone = ?", (telefone,))
    conexao.commit()
    conexao.close()

def atualizarcliente(telefone, nome, email):
    conexao = sqlite3.connect("exemplo.tp")
    produto = conexao.produto()
    produto.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (nome, email, telefone))
    conexao.commit()
    conexao.close()

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        adicionarcliente(nome,email)
        print("Cliente adicionado com sucesso!")
    
    elif escolha == "2":
        print("\nTodos os clientes:")
        listarcliente()
    
    elif escolha == "3":
        telefone = int("Digite seu telefone a ser atualizado: ")
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        atualizarcliente(telefone, nome, email)
        print("Cliente atualizado com sucesso")

    elif escolha == "4":
        telefone = int("Digite o telefone do cliente a ser deletado: ")
        deletarcliente(telefone)
        print("Cliente deletado com sucesso!")
    elif escolha == "5":
        print("Deseja sair do site?")
        break
    else:
        print("Opção inválida. Tente novamente")
