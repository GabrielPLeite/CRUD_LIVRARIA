#PROJETO LIVRARIA "UNIVERSO LITERARIO"

# Dicionário para armazenar os livros
livros = {}

# Dicionário para armazenar o carrinho de compras
carrinho = {}  


# Função para incluir um novo livro
def incluir_livro():
    nome    = input("Digite o nome do livro: ")
    autor   = input("Digite o nome do autor: ")
    sessao  = input("Digite a sessão do livro: ")
    # Validação de dados para o preço
    while True:
        try:
            preco   = float(input("Digite o preço do livro: R$"))
            break
        except:
            print("Valor inválido")
            print("Digite o preço do livro: R$")
    # Inclusão do livro no dicionário
    livros[nome] = {'autor': autor,'sessao' : sessao,'preco': preco}
    print(f"{nome} foi incluído com sucesso!")

# Função para editar um livro existente
def editar_livro():
    nome = input("Digite o nome do livro: ")
    if nome in livros:
        autor   = input("Novo autor: ")
        sessao  = input("Nova sessão: ")
        # Validação de dados para o novo preço
        while True:
            try:
                preco   = float(input("Novo preço: R$"))
                break
            except:
                print("Valor inválido")
                print("Novo preço: R$")
        # Atualização do livro no dicionário
        livros[nome] = {'autor': autor, 'sessao' : sessao,'preco': preco}
        print(f"{nome} editado com sucesso!!")
    else:
        print("Livro não encontrado")

# Função para excluir um livro do dicionário       
def excluir_livro():
    nome = input("Digite o nome do livro: ")
    if nome in livros:
        del livros[nome]
    else:
        print("Livro não encontrado")

# Função para buscar um livro do dicionário 
def buscar_livro():
    nome = input("Digite o nome do livro: ")
    if nome in livros:
        livros[nome]
    else:
        print("Livro não encontrado")

# Função para adicionar um livro ao carrinho
def adicionar_ao_carrinho():
    nome = input("Digite o nome do livro: ")
    if nome in livros:
        preco = livros[nome]['preco']
        # Verificar se o livro ja esta no carrinho
        if nome in carrinho:
            carrinho[nome] += preco
        else:
            carrinho[nome] = preco

        print(f'{nome} adicionado com sucesso')
        total = sum(carrinho.values())
        # Verificar quanto falta para o desconto
        if total < 300:
            diferenca = 300 - total
            print(f'Faltam R${diferenca:.2f} para atingir o desconto de 10%')
        else:
            print('Voce esta elegivel ao desconto de 10%')

    else:
        print("Livro não encontrado")

# Função para finalizar a compra
def finalizar_compra():
    if len(carrinho) >= 1:
        total = sum(carrinho.values())
        if total >= 300:
            desconto = total*0.1
            total = total - desconto
            print('Livros no carrinho ...................')
            for nome_livro, valor_livro in carrinho.items():
                print(f'{nome_livro} - R$ {valor_livro:.2f}')
            print(f'Total - R$ {sum(carrinho.values()):.2f}')
            print(f'Você teve um desconto de: R$ {desconto:.2f}')
            print(f'O valor final ficou R$ {total:.2f}')
            confirmacao = input("Confirma? [s/n]: ")
            confirmacao_M = confirmacao.upper()

        else:
            for nome_livro, valor_livro in carrinho.items():
                print(f'{nome_livro} - {valor_livro}')
            print(f'Total - {sum(carrinho.values())}')
            confirmacao = input("Confirma? [s/n]: ")
            confirmacao_M = confirmacao.upper()
        
        if confirmacao_M == "S":
            print ("Compra confirmada !!")
        else:
            print("Compra cancelada")
    else:
        print("Você ainda não adicionou nada no carrinho")

# Função para exibir o menu de opções
def exibir_menu():
    print("=======================================================================")
    print("1. Incluir livro")
    print("2. Editar livro")
    print("3. Excluir livro")
    print("4. Buscar livro")
    print("5. Adicionar ao carrinho")
    print("6. Finalizar compra")
    print("7. Sair")

# Boas vindas ao usuário
print("                   Bem vindo ao Universo Literário                     ")

# Programa Principal
while True:
    exibir_menu()
    opcao = input("Selecione uma opção: ")
    if opcao == '7':
        print("Programa finalizado ...")
        break
    elif opcao == '1': 
        incluir_livro ()
    elif opcao == '2':
        editar_livro()
    elif opcao == '3':
        excluir_livro()
    elif opcao == '4':
        buscar_livro()
    elif opcao == '5':
        adicionar_ao_carrinho()
    elif opcao == '6':
        finalizar_compra()
    else:
        print("Opção inválida")

