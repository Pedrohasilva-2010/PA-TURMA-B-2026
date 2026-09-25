nomes = []
idades = []

while True:
    print("\n1- Cadastrar | 2- Listar maiores de 18 | 3- Sair")
    opcao = input("Opção: ")
    
    if opcao == '1':
        nomes.append(input("Nome: "))
        idades.append(int(input("Idade: ")))
    elif opcao == '2':
        print("\n--- Maiores de 18 anos ---")
        for i in range(len(nomes)):
            if idades[i] > 18:
                print(f"{nomes[i]} - {idades[i]} anos")
    elif opcao == '3':
        break