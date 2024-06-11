'''                      Sistema para cadastro de produtos
voce foi contratado para desenvolver um sistema de cadastro de produtos para determinar
loja, que deve ser capaz de armazenar informações com nome, categoria, preco, e quantidade
em estoque. O sistema deve oferecer um menu interativo com as seguintes opções:

1. Cadastro de novo produto
2. Editar dados de um produto 
3. Excluir um produto
4. Listar todos produtos cadastrados
5. Efetuar venda
6. Sair do sistema
'''

produtos = []

while True:
    print('---------------------------------------------------')
    print("|                 MENU PRINCIPAL                  |")
    print('|-------------------------------------------------|')
    print("|          1. Cadastro de novo produto            |")
    print("|          2. Editar dados de um produto          |")
    print("|          3. Excluir um produto                  |")
    print("|          4. Listar todos produtos cadastrados   |")
    print("|          5. Efetuar uma venda                   |")
    print("|          6. Sair do sistema                     |")
    print('---------------------------------------------------')
    print()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome do produto: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        for produto in produtos:
            if produto["nome"] == nome:
                print("Erro: Produto já cadastrado.")
                break
        else:
            produtos.append({"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade})
            print("Produto cadastrado com sucesso.")
    
    elif opcao == "2":
        print('-----------------------------------------')
        print('|            EDITAR PRODUTO             |')
        print('-----------------------------------------')
        nome = input("Digite o nome do produto a ser editado: ")
        for produto in produtos:
            if produto["nome"] == nome:
                print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
                print('--------------------------------------------')
                print("|                 MENU EDIÇÂO              |")
                print("|            1. Editar nome                |")
                print("|            2. Editar categoria           |")
                print("|            3. Editar preço|              |")
                print("|            4. Editar quantidade          |")
                print("|            5. Voltar ao menu principal   |")
                print('--------------------------------------------')
                
                opcao_edicao = input("Escolha uma opção de edição: ")
                if opcao_edicao == "1":
                    novo_nome = input("Novo nome: ")
                    produto["nome"] = novo_nome
                    print("Nome do produto editado com sucesso.")
                elif opcao_edicao == "2":
                    nova_categoria = input("Nova categoria: ")
                    produto["categoria"] = nova_categoria
                    print("Categoria do produto editada com sucesso.")
                elif opcao_edicao == "3":
                    novo_preco = float(input("Novo preço: "))
                    produto["preco"] = novo_preco
                    print("Preço do produto editado com sucesso.")
                elif opcao_edicao == "4":
                    nova_quantidade = int(input("Nova quantidade: "))
                    produto["quantidade"] = nova_quantidade
                    print("Quantidade do produto editada com sucesso.")
                elif opcao_edicao == "5":
                    break
                else:
                    print("Opção inválida.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome do produto a ser excluído: ")
        for produto in produtos:
            if produto["nome"] == nome:
                produtos.remove(produto)
                print("Produto excluído com sucesso.")
                break
        else:
            print("Produto não encontrado.")
    
    elif opcao == "4":
        if produtos:
            print("--- LISTA DE PRODUTOS ---")
            for produto in produtos:
                print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
        else:
            print("Nenhum produto cadastrado.")
    
    elif opcao == "5":
        nome = input("Digite o nome do produto vendido: ")
        for produto in produtos:
            if produto["nome"] == nome:
                quantidade_vendida = int(input("Digite a quantidade vendida: "))
                if quantidade_vendida > produto["quantidade"]:
                    print("Quantidade insuficiente em estoque.")
                else:
                    valor_total = quantidade_vendida * produto["preco"]
                    print(f"Valor total da compra: R${valor_total}")
                    produto["quantidade"] -= quantidade_vendida
                    print("Venda realizada com sucesso.")
                break

        else:
            print("Produto não encontrado.")
    
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida.")
