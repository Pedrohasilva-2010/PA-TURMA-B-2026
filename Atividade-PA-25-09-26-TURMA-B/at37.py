produtos = []
quantidades = []

while True:
    print("\n1- Adicionar Produto | 2- Dar Baixa | 3- Ver Estoque | 4- Sair")
    opcao = input("Opção: ")
    
    if opcao == '1':
        produtos.append(input("Nome do produto: "))
        quantidades.append(int(input("Quantidade: ")))
    elif opcao == '2':
        nome = input("Nome do produto para dar baixa: ")
        if nome in produtos:
            idx = produtos.index(nome)
            qtd = int(input("Quantidade a retirar: "))
            if quantidades[idx] >= qtd:
                quantidades[idx] -= qtd
                print("Baixa realizada!")
            else:
                print("Estoque insuficiente!")
        else:
            print("Produto não encontrado!")
    elif opcao == '3':
        print("\n--- Estoque ---")
        for i in range(len(produtos)):
            print(f"{produtos[i]}: {quantidades[i]} un.")
    elif opcao == '4':
        break